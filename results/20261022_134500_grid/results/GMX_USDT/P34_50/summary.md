# EMA Hourly Continuation — GMX/USDT P34_50

**Symbol:** GMX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.3391 |
| net_win_rate | 0.3899 |
| gross_profit_factor | 0.7337 |
| gross_win_rate | 0.4179 |
| sharpe_ratio | -9.8851 |
| sortino_ratio | -4.2277 |
| max_drawdown | 0.9951 |
| cagr | -0.8783 |
| net_avg_win | 14.6305 |
| net_avg_loss | -27.5744 |
| avg_hold_time_bars | 3.2022 |
| exposure | 0.1303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
