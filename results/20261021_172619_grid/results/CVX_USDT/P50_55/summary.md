# EMA Hourly Continuation — CVX/USDT P50_55

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 143 |
| net_profit_factor | 1.0232 |
| net_win_rate | 0.6014 |
| gross_profit_factor | 1.4915 |
| gross_win_rate | 0.6014 |
| sharpe_ratio | 0.1268 |
| sortino_ratio | 0.0223 |
| max_drawdown | 0.1336 |
| cagr | 0.0067 |
| net_avg_win | 87.4626 |
| net_avg_loss | -128.9740 |
| avg_hold_time_bars | 4.5944 |
| exposure | 0.0299 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
