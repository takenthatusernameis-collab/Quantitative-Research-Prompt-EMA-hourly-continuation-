# EMA Hourly Continuation — LSK/USDT P55_144

**Symbol:** LSK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7371 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -1.6166 |
| sortino_ratio | -0.4493 |
| max_drawdown | 0.4878 |
| cagr | -0.1874 |
| net_avg_win | 59.9292 |
| net_avg_loss | -83.0509 |
| avg_hold_time_bars | 15.4229 |
| exposure | 0.2636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
