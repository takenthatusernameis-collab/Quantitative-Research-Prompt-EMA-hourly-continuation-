# EMA Hourly Continuation — AGLD/USDT P20_144

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7909 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -1.7665 |
| sortino_ratio | -0.5297 |
| max_drawdown | 0.5378 |
| cagr | -0.2168 |
| net_avg_win | 80.9596 |
| net_avg_loss | -96.1043 |
| avg_hold_time_bars | 27.0135 |
| exposure | 0.5428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
