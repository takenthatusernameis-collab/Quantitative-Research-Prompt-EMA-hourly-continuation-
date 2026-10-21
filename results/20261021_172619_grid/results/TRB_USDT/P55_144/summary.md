# EMA Hourly Continuation — TRB/USDT P55_144

**Symbol:** TRB/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6979 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -2.1578 |
| sortino_ratio | -0.5863 |
| max_drawdown | 0.5308 |
| cagr | -0.2355 |
| net_avg_win | 65.7283 |
| net_avg_loss | -84.8562 |
| avg_hold_time_bars | 14.3342 |
| exposure | 0.2368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
