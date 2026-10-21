# EMA Hourly Continuation — WLD/USDT P12_144

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 1.0079 |
| net_win_rate | 0.5343 |
| gross_profit_factor | 1.1342 |
| gross_win_rate | 0.5343 |
| sharpe_ratio | 0.1081 |
| sortino_ratio | 0.0292 |
| max_drawdown | 0.2399 |
| cagr | 0.0058 |
| net_avg_win | 100.2311 |
| net_avg_loss | -114.0905 |
| avg_hold_time_bars | 42.5457 |
| exposure | 0.6769 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
