# EMA Hourly Continuation — DUSK/USDT P34_200

**Symbol:** DUSK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7821 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9899 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -1.3849 |
| sortino_ratio | -0.3511 |
| max_drawdown | 0.3973 |
| cagr | -0.1505 |
| net_avg_win | 77.3292 |
| net_avg_loss | -95.8040 |
| avg_hold_time_bars | 37.4069 |
| exposure | 0.5390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
