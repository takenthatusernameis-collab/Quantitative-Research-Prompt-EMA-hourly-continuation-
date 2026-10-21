# EMA Hourly Continuation — MANA/USDT P8_21

**Symbol:** MANA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.7134 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0207 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -2.4483 |
| sortino_ratio | -0.8200 |
| max_drawdown | 0.6077 |
| cagr | -0.3111 |
| net_avg_win | 55.4159 |
| net_avg_loss | -78.8323 |
| avg_hold_time_bars | 5.5554 |
| exposure | 0.1369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
