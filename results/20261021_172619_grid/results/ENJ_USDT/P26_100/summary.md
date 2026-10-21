# EMA Hourly Continuation — ENJ/USDT P26_100

**Symbol:** ENJ/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.7975 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0096 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5814 |
| sortino_ratio | -0.4835 |
| max_drawdown | 0.4775 |
| cagr | -0.2000 |
| net_avg_win | 74.0424 |
| net_avg_loss | -92.8389 |
| avg_hold_time_bars | 17.0131 |
| exposure | 0.3526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
