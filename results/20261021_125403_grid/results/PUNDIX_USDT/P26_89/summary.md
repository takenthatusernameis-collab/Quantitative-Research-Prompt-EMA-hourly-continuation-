# EMA Hourly Continuation — PUNDIX/USDT P26_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.6768 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.9222 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.8714 |
| sortino_ratio | -0.9504 |
| max_drawdown | 0.6759 |
| cagr | -0.3531 |
| net_avg_win | 54.1793 |
| net_avg_loss | -73.4795 |
| avg_hold_time_bars | 13.8566 |
| exposure | 0.3382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
