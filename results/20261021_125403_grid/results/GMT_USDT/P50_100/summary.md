# EMA Hourly Continuation — GMT/USDT P50_100

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7793 |
| net_win_rate | 0.5055 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.5055 |
| sharpe_ratio | -1.5814 |
| sortino_ratio | -0.4321 |
| max_drawdown | 0.4535 |
| cagr | -0.1802 |
| net_avg_win | 75.7962 |
| net_avg_loss | -99.4352 |
| avg_hold_time_bars | 8.5608 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
