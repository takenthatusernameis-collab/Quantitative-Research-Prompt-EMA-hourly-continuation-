# EMA Hourly Continuation — PYTH/USDT P21_200

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 1.0421 |
| net_win_rate | 0.5462 |
| gross_profit_factor | 1.1899 |
| gross_win_rate | 0.5462 |
| sharpe_ratio | 0.2620 |
| sortino_ratio | 0.0600 |
| max_drawdown | 0.1333 |
| cagr | 0.0213 |
| net_avg_win | 99.0261 |
| net_avg_loss | -114.3680 |
| avg_hold_time_bars | 59.3574 |
| exposure | 0.6718 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
