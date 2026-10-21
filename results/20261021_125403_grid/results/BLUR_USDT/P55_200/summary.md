# EMA Hourly Continuation — BLUR/USDT P55_200

**Symbol:** BLUR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 1.0210 |
| net_win_rate | 0.5526 |
| gross_profit_factor | 1.2183 |
| gross_win_rate | 0.5526 |
| sharpe_ratio | 0.1610 |
| sortino_ratio | 0.0380 |
| max_drawdown | 0.1331 |
| cagr | 0.0113 |
| net_avg_win | 95.4401 |
| net_avg_loss | -115.4721 |
| avg_hold_time_bars | 33.7368 |
| exposure | 0.4061 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
