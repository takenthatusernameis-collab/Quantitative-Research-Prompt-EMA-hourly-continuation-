# EMA Hourly Continuation — HNT/USDT P21_144

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7624 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -1.4459 |
| sortino_ratio | -0.3837 |
| max_drawdown | 0.4275 |
| cagr | -0.1630 |
| net_avg_win | 69.2184 |
| net_avg_loss | -83.7702 |
| avg_hold_time_bars | 33.6695 |
| exposure | 0.5326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
