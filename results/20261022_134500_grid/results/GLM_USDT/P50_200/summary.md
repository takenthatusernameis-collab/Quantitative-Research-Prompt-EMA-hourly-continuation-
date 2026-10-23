# EMA Hourly Continuation — GLM/USDT P50_200

**Symbol:** GLM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6406 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -2.8248 |
| sortino_ratio | -0.8063 |
| max_drawdown | 0.6258 |
| cagr | -0.3169 |
| net_avg_win | 56.5974 |
| net_avg_loss | -79.7168 |
| avg_hold_time_bars | 20.0489 |
| exposure | 0.3727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
