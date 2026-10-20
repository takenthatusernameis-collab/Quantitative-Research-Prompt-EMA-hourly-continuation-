# EMA Hourly Continuation — ANKR/USDT P34_89

**Symbol:** ANKR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.5053 |
| net_win_rate | 0.4316 |
| gross_profit_factor | 0.8792 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -6.5503 |
| sortino_ratio | -2.4567 |
| max_drawdown | 0.9516 |
| cagr | -0.6995 |
| net_avg_win | 31.7447 |
| net_avg_loss | -47.7058 |
| avg_hold_time_bars | 8.8364 |
| exposure | 0.2848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
