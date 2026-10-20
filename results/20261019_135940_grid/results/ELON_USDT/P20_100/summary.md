# EMA Hourly Continuation — ELON/USDT P20_100

**Symbol:** ELON/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.5176 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8114 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -5.6066 |
| sortino_ratio | -2.1444 |
| max_drawdown | 0.9297 |
| cagr | -0.6446 |
| net_avg_win | 30.5584 |
| net_avg_loss | -46.2348 |
| avg_hold_time_bars | 10.9784 |
| exposure | 0.3693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
