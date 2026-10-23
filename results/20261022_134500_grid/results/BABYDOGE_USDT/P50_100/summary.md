# EMA Hourly Continuation — BABYDOGE/USDT P50_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 34 |
| net_profit_factor | 1.1493 |
| net_win_rate | 0.5588 |
| gross_profit_factor | 1.2537 |
| gross_win_rate | 0.5588 |
| sharpe_ratio | 0.2733 |
| sortino_ratio | 0.0232 |
| max_drawdown | 0.0354 |
| cagr | 0.0094 |
| net_avg_win | 96.6705 |
| net_avg_loss | -106.5431 |
| avg_hold_time_bars | 16.6176 |
| exposure | 0.0256 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
