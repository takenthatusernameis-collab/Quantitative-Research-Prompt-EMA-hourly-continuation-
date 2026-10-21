# EMA Hourly Continuation — POL/USDT P21_200

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 1.0354 |
| net_win_rate | 0.5517 |
| gross_profit_factor | 1.2298 |
| gross_win_rate | 0.5517 |
| sharpe_ratio | 0.2164 |
| sortino_ratio | 0.0508 |
| max_drawdown | 0.1790 |
| cagr | 0.0170 |
| net_avg_win | 87.6038 |
| net_avg_loss | -104.1311 |
| avg_hold_time_bars | 55.7356 |
| exposure | 0.6612 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
