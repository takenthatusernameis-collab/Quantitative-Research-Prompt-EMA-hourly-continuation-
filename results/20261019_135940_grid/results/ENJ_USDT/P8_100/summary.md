# EMA Hourly Continuation — ENJ/USDT P8_100

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.6398 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -3.7972 |
| sortino_ratio | -1.3631 |
| max_drawdown | 0.8181 |
| cagr | -0.4808 |
| net_avg_win | 46.0982 |
| net_avg_loss | -65.3311 |
| avg_hold_time_bars | 22.7875 |
| exposure | 0.6774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
