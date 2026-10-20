# EMA Hourly Continuation — VELO/USDT P8_200

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7936 |
| net_win_rate | 0.5103 |
| gross_profit_factor | 1.0479 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.5302 |
| sortino_ratio | -0.4777 |
| max_drawdown | 0.5363 |
| cagr | -0.2038 |
| net_avg_win | 67.5535 |
| net_avg_loss | -88.7017 |
| avg_hold_time_bars | 33.9074 |
| exposure | 0.7490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
