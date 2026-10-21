# EMA Hourly Continuation — LUNC/USDT P21_34

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7129 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -3.4514 |
| sortino_ratio | -0.7917 |
| max_drawdown | 0.6159 |
| cagr | -0.3071 |
| net_avg_win | 58.0396 |
| net_avg_loss | -80.4610 |
| avg_hold_time_bars | 4.7220 |
| exposure | 0.0556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
