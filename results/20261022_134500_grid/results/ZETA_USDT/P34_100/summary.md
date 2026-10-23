# EMA Hourly Continuation — ZETA/USDT P34_100

**Symbol:** ZETA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 666 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.9784 |
| gross_win_rate | 0.4700 |
| sharpe_ratio | -4.3778 |
| sortino_ratio | -1.5881 |
| max_drawdown | 0.8639 |
| cagr | -0.5313 |
| net_avg_win | 54.3790 |
| net_avg_loss | -70.5871 |
| avg_hold_time_bars | 9.1051 |
| exposure | 0.2744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
