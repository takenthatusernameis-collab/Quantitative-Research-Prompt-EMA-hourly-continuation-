# EMA Hourly Continuation — ZETA/USDT P20_89

**Symbol:** ZETA/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8555 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0679 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -1.1817 |
| sortino_ratio | -0.3722 |
| max_drawdown | 0.4817 |
| cagr | -0.1594 |
| net_avg_win | 84.6493 |
| net_avg_loss | -104.4251 |
| avg_hold_time_bars | 19.4493 |
| exposure | 0.4251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
