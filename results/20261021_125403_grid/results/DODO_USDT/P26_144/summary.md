# EMA Hourly Continuation — DODO/USDT P26_144

**Symbol:** DODO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.7000 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.8598 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -2.5557 |
| sortino_ratio | -0.7462 |
| max_drawdown | 0.6086 |
| cagr | -0.2903 |
| net_avg_win | 70.0018 |
| net_avg_loss | -82.8327 |
| avg_hold_time_bars | 22.5282 |
| exposure | 0.4343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
