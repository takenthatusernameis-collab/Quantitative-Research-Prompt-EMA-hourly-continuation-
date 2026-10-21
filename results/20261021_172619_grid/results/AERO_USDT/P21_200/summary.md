# EMA Hourly Continuation — AERO/USDT P21_200

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 1.0122 |
| net_win_rate | 0.5396 |
| gross_profit_factor | 1.1610 |
| gross_win_rate | 0.5396 |
| sharpe_ratio | 0.1196 |
| sortino_ratio | 0.0282 |
| max_drawdown | 0.1854 |
| cagr | 0.0070 |
| net_avg_win | 102.8603 |
| net_avg_loss | -119.1100 |
| avg_hold_time_bars | 51.9472 |
| exposure | 0.6257 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
