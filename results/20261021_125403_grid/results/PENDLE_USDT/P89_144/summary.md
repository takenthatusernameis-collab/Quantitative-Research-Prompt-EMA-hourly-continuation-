# EMA Hourly Continuation — PENDLE/USDT P89_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6589 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8401 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -2.0530 |
| sortino_ratio | -0.4867 |
| max_drawdown | 0.4291 |
| cagr | -0.2001 |
| net_avg_win | 64.7672 |
| net_avg_loss | -84.4391 |
| avg_hold_time_bars | 7.4982 |
| exposure | 0.0944 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
