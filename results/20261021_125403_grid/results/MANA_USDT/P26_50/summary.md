# EMA Hourly Continuation — MANA/USDT P26_50

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0157 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -2.2421 |
| sortino_ratio | -0.6586 |
| max_drawdown | 0.5542 |
| cagr | -0.2589 |
| net_avg_win | 61.8387 |
| net_avg_loss | -87.5613 |
| avg_hold_time_bars | 6.5564 |
| exposure | 0.1243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
