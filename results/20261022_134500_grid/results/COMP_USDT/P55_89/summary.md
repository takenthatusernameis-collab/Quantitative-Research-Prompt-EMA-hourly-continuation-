# EMA Hourly Continuation — COMP/USDT P55_89

**Symbol:** COMP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.3990 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8555 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -6.1381 |
| sortino_ratio | -2.2972 |
| max_drawdown | 0.9451 |
| cagr | -0.6812 |
| net_avg_win | 18.6385 |
| net_avg_loss | -41.7449 |
| avg_hold_time_bars | 4.0632 |
| exposure | 0.1315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
