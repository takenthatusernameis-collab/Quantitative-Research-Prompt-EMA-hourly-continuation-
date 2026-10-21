# EMA Hourly Continuation — BLUR/USDT P21_200

**Symbol:** BLUR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 1.0199 |
| net_win_rate | 0.5511 |
| gross_profit_factor | 1.2092 |
| gross_win_rate | 0.5511 |
| sharpe_ratio | 0.1528 |
| sortino_ratio | 0.0366 |
| max_drawdown | 0.1425 |
| cagr | 0.0105 |
| net_avg_win | 91.2181 |
| net_avg_loss | -109.8030 |
| avg_hold_time_bars | 54.7883 |
| exposure | 0.6793 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
