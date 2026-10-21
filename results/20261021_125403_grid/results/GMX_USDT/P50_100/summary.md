# EMA Hourly Continuation — GMX/USDT P50_100

**Symbol:** GMX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.5534 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.7598 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -3.6328 |
| sortino_ratio | -1.0716 |
| max_drawdown | 0.7173 |
| cagr | -0.3893 |
| net_avg_win | 46.5522 |
| net_avg_loss | -65.9742 |
| avg_hold_time_bars | 8.8535 |
| exposure | 0.1730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
