# EMA Hourly Continuation — EUL/USDT P26_50

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6710 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -2.1314 |
| sortino_ratio | -0.6175 |
| max_drawdown | 0.5188 |
| cagr | -0.2461 |
| net_avg_win | 51.5554 |
| net_avg_loss | -74.2473 |
| avg_hold_time_bars | 6.9315 |
| exposure | 0.1289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
