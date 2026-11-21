# EMA Hourly Continuation — HTR/USDT P26_34

**Symbol:** HTR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.2458 |
| net_win_rate | 0.3313 |
| gross_profit_factor | 0.5651 |
| gross_win_rate | 0.3558 |
| sharpe_ratio | -12.7046 |
| sortino_ratio | -5.7022 |
| max_drawdown | 0.9994 |
| cagr | -0.9491 |
| net_avg_win | 10.0225 |
| net_avg_loss | -20.2007 |
| avg_hold_time_bars | 2.7513 |
| exposure | 0.1227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
