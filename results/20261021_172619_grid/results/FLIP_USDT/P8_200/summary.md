# EMA Hourly Continuation — FLIP/USDT P8_200

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9077 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -1.2412 |
| sortino_ratio | -0.2445 |
| max_drawdown | 0.2745 |
| cagr | -0.1095 |
| net_avg_win | 82.3032 |
| net_avg_loss | -100.6261 |
| avg_hold_time_bars | 92.4439 |
| exposure | 0.8236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
