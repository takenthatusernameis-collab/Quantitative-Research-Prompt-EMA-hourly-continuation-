# EMA Hourly Continuation — BTT/USDT P8_12

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.4151 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.8220 |
| gross_win_rate | 0.4034 |
| sharpe_ratio | -5.6985 |
| sortino_ratio | -1.4340 |
| max_drawdown | 0.8263 |
| cagr | -0.4987 |
| net_avg_win | 49.5154 |
| net_avg_loss | -79.5318 |
| avg_hold_time_bars | 5.1424 |
| exposure | 0.0690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
