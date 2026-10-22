# EMA Hourly Continuation — POL/USDT P8_200

**Symbol:** POL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.6955 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9649 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9265 |
| sortino_ratio | -0.4905 |
| max_drawdown | 0.5122 |
| cagr | -0.2096 |
| net_avg_win | 62.8916 |
| net_avg_loss | -88.2447 |
| avg_hold_time_bars | 55.4451 |
| exposure | 0.8266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
