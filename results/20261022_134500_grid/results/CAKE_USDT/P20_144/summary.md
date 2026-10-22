# EMA Hourly Continuation — CAKE/USDT P20_144

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6389 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9632 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -3.1989 |
| sortino_ratio | -0.9828 |
| max_drawdown | 0.7349 |
| cagr | -0.3810 |
| net_avg_win | 52.9566 |
| net_avg_loss | -76.9607 |
| avg_hold_time_bars | 23.7510 |
| exposure | 0.5247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
