# EMA Hourly Continuation — ELON/USDT P8_89

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 880 |
| net_profit_factor | 0.5394 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8002 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -5.9027 |
| sortino_ratio | -2.4636 |
| max_drawdown | 0.9489 |
| cagr | -0.6928 |
| net_avg_win | 28.7003 |
| net_avg_loss | -41.7661 |
| avg_hold_time_bars | 14.4102 |
| exposure | 0.5764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
