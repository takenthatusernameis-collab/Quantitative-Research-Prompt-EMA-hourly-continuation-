# EMA Hourly Continuation — POPCAT/USDT P12_21

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6730 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8855 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.6758 |
| sortino_ratio | -0.7225 |
| max_drawdown | 0.5301 |
| cagr | -0.2836 |
| net_avg_win | 74.4499 |
| net_avg_loss | -94.0574 |
| avg_hold_time_bars | 5.0680 |
| exposure | 0.0827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
