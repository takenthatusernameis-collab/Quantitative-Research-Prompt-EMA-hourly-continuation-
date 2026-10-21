# EMA Hourly Continuation — FET/USDT P12_144

**Symbol:** FET/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 1.0089 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1393 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | 0.1036 |
| sortino_ratio | 0.0258 |
| max_drawdown | 0.1261 |
| cagr | 0.0054 |
| net_avg_win | 96.6268 |
| net_avg_loss | -109.5571 |
| avg_hold_time_bars | 54.0973 |
| exposure | 0.7328 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
