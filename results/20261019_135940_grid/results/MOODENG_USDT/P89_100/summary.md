# EMA Hourly Continuation — MOODENG/USDT P89_100

**Symbol:** MOODENG/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.4408 |
| net_win_rate | 0.4225 |
| gross_profit_factor | 0.8407 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -6.9982 |
| sortino_ratio | -2.4466 |
| max_drawdown | 0.9216 |
| cagr | -0.7058 |
| net_avg_win | 34.5313 |
| net_avg_loss | -57.3173 |
| avg_hold_time_bars | 2.3078 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
