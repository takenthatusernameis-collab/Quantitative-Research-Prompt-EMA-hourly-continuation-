# EMA Hourly Continuation — ELON/USDT P26_89

**Symbol:** ELON/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.9171 |
| sortino_ratio | -0.8593 |
| max_drawdown | 0.6408 |
| cagr | -0.3261 |
| net_avg_win | 58.3858 |
| net_avg_loss | -75.5278 |
| avg_hold_time_bars | 13.4336 |
| exposure | 0.2620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
