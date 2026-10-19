# EMA Hourly Continuation — COMP/USDT P55_144

**Symbol:** COMP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.5726 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9860 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -3.6149 |
| sortino_ratio | -1.1512 |
| max_drawdown | 0.7769 |
| cagr | -0.4299 |
| net_avg_win | 39.8790 |
| net_avg_loss | -67.5216 |
| avg_hold_time_bars | 11.1860 |
| exposure | 0.2624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
