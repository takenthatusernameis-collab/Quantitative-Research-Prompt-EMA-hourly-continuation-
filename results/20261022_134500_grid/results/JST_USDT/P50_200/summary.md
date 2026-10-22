# EMA Hourly Continuation — JST/USDT P50_200

**Symbol:** JST/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.5545 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0285 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -3.0491 |
| sortino_ratio | -0.8155 |
| max_drawdown | 0.6288 |
| cagr | -0.3249 |
| net_avg_win | 43.0073 |
| net_avg_loss | -78.8572 |
| avg_hold_time_bars | 24.3352 |
| exposure | 0.3975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
