# EMA Hourly Continuation — TFUEL/USDT P21_200

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.7572 |
| gross_win_rate | 0.4228 |
| sharpe_ratio | -3.4467 |
| sortino_ratio | -0.9953 |
| max_drawdown | 0.6969 |
| cagr | -0.3693 |
| net_avg_win | 60.6276 |
| net_avg_loss | -72.6953 |
| avg_hold_time_bars | 28.0475 |
| exposure | 0.5343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
