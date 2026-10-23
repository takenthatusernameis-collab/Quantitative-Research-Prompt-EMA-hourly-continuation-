# EMA Hourly Continuation — DUSK/USDT P21_89

**Symbol:** DUSK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.6530 |
| net_win_rate | 0.4608 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -3.9985 |
| sortino_ratio | -1.5059 |
| max_drawdown | 0.8467 |
| cagr | -0.5084 |
| net_avg_win | 47.5768 |
| net_avg_loss | -62.2653 |
| avg_hold_time_bars | 10.8585 |
| exposure | 0.3524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
