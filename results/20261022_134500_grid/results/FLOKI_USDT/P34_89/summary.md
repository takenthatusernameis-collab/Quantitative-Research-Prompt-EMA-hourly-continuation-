# EMA Hourly Continuation — FLOKI/USDT P34_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.6142 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9309 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -4.4188 |
| sortino_ratio | -1.6492 |
| max_drawdown | 0.8693 |
| cagr | -0.5477 |
| net_avg_win | 41.4124 |
| net_avg_loss | -60.1755 |
| avg_hold_time_bars | 8.5767 |
| exposure | 0.2745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
