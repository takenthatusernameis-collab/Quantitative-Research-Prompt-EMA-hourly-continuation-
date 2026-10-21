# EMA Hourly Continuation — CETUS/USDT P8_200

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 1.2740 |
| net_win_rate | 0.5882 |
| gross_profit_factor | 1.4345 |
| gross_win_rate | 0.5882 |
| sharpe_ratio | 1.1430 |
| sortino_ratio | 0.2504 |
| max_drawdown | 0.1125 |
| cagr | 0.1076 |
| net_avg_win | 105.1616 |
| net_avg_loss | -117.9194 |
| avg_hold_time_bars | 83.7240 |
| exposure | 0.8373 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
