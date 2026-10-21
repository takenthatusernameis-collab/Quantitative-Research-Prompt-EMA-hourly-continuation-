# EMA Hourly Continuation — DEGEN/USDT P12_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.8266 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9813 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -1.6446 |
| sortino_ratio | -0.5718 |
| max_drawdown | 0.5246 |
| cagr | -0.2336 |
| net_avg_win | 79.7289 |
| net_avg_loss | -93.2516 |
| avg_hold_time_bars | 13.1537 |
| exposure | 0.3545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
