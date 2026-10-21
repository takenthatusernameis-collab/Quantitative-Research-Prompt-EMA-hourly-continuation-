# EMA Hourly Continuation — XYO/USDT P50_200

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.5890 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.7748 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -3.0134 |
| sortino_ratio | -0.8144 |
| max_drawdown | 0.6311 |
| cagr | -0.3136 |
| net_avg_win | 54.2270 |
| net_avg_loss | -73.4678 |
| avg_hold_time_bars | 22.5726 |
| exposure | 0.3728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
