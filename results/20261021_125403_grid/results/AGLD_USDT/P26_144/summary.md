# EMA Hourly Continuation — AGLD/USDT P26_144

**Symbol:** AGLD/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7513 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.9247 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -2.1102 |
| sortino_ratio | -0.6323 |
| max_drawdown | 0.5852 |
| cagr | -0.2521 |
| net_avg_win | 74.3476 |
| net_avg_loss | -89.2360 |
| avg_hold_time_bars | 23.2584 |
| exposure | 0.4684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
