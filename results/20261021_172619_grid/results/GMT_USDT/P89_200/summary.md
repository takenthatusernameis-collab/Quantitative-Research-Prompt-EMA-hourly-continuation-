# EMA Hourly Continuation — GMT/USDT P89_200

**Symbol:** GMT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.8299 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0416 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -0.8963 |
| sortino_ratio | -0.2112 |
| max_drawdown | 0.2636 |
| cagr | -0.0939 |
| net_avg_win | 76.9921 |
| net_avg_loss | -98.4347 |
| avg_hold_time_bars | 15.9593 |
| exposure | 0.1959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
