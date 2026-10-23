# EMA Hourly Continuation — MAGIC/USDT P12_144

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7465 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0029 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.1574 |
| sortino_ratio | -0.6730 |
| max_drawdown | 0.6216 |
| cagr | -0.2695 |
| net_avg_win | 67.2266 |
| net_avg_loss | -88.2067 |
| avg_hold_time_bars | 31.1056 |
| exposure | 0.6829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
