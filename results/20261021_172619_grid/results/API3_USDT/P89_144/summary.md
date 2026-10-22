# EMA Hourly Continuation — API3/USDT P89_144

**Symbol:** API3/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.8264 |
| net_win_rate | 0.5309 |
| gross_profit_factor | 1.1046 |
| gross_win_rate | 0.5309 |
| sharpe_ratio | -0.9395 |
| sortino_ratio | -0.2377 |
| max_drawdown | 0.3075 |
| cagr | -0.1046 |
| net_avg_win | 70.7615 |
| net_avg_loss | -96.9264 |
| avg_hold_time_bars | 6.8893 |
| exposure | 0.0961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
