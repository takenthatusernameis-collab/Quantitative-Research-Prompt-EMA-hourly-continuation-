# EMA Hourly Continuation — GMX/USDT P26_34

**Symbol:** GMX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5541 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -3.5085 |
| sortino_ratio | -0.9124 |
| max_drawdown | 0.6524 |
| cagr | -0.3411 |
| net_avg_win | 54.1588 |
| net_avg_loss | -80.9041 |
| avg_hold_time_bars | 4.7964 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
