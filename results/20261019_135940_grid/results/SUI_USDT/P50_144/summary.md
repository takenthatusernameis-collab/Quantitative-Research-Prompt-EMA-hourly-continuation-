# EMA Hourly Continuation — SUI/USDT P50_144

**Symbol:** SUI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6076 |
| net_win_rate | 0.4691 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -3.8338 |
| sortino_ratio | -1.2269 |
| max_drawdown | 0.7909 |
| cagr | -0.4464 |
| net_avg_win | 49.2946 |
| net_avg_loss | -71.6848 |
| avg_hold_time_bars | 10.6409 |
| exposure | 0.2505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
