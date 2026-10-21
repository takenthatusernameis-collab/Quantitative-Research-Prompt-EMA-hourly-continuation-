# EMA Hourly Continuation — REZ/USDT P21_144

**Symbol:** REZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 1.0045 |
| net_win_rate | 0.5422 |
| gross_profit_factor | 1.1731 |
| gross_win_rate | 0.5422 |
| sharpe_ratio | 0.0900 |
| sortino_ratio | 0.0252 |
| max_drawdown | 0.1784 |
| cagr | 0.0035 |
| net_avg_win | 99.2938 |
| net_avg_loss | -117.0925 |
| avg_hold_time_bars | 31.9564 |
| exposure | 0.5411 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
