# EMA Hourly Continuation — AVAX/USDT P55_144

**Symbol:** AVAX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8888 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -4.4807 |
| sortino_ratio | -1.3497 |
| max_drawdown | 0.8173 |
| cagr | -0.4797 |
| net_avg_win | 49.2199 |
| net_avg_loss | -73.0016 |
| avg_hold_time_bars | 11.1094 |
| exposure | 0.2308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
