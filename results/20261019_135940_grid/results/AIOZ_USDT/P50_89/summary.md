# EMA Hourly Continuation — AIOZ/USDT P50_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.6433 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 1.0182 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -5.2492 |
| sortino_ratio | -2.0520 |
| max_drawdown | 0.9223 |
| cagr | -0.6282 |
| net_avg_win | 45.9306 |
| net_avg_loss | -63.6175 |
| avg_hold_time_bars | 4.5550 |
| exposure | 0.1582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
