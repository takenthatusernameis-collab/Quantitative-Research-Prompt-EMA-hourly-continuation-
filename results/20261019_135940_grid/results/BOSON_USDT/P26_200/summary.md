# EMA Hourly Continuation — BOSON/USDT P26_200

**Symbol:** BOSON/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.7583 |
| net_win_rate | 0.4797 |
| gross_profit_factor | 0.9707 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -2.0052 |
| sortino_ratio | -0.6131 |
| max_drawdown | 0.5157 |
| cagr | -0.2508 |
| net_avg_win | 71.9112 |
| net_avg_loss | -87.4480 |
| avg_hold_time_bars | 23.6610 |
| exposure | 0.5044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
