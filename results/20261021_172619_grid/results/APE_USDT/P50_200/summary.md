# EMA Hourly Continuation — APE/USDT P50_200

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.7763 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -1.3051 |
| sortino_ratio | -0.3273 |
| max_drawdown | 0.3286 |
| cagr | -0.1410 |
| net_avg_win | 73.4189 |
| net_avg_loss | -89.2167 |
| avg_hold_time_bars | 28.3269 |
| exposure | 0.3979 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
