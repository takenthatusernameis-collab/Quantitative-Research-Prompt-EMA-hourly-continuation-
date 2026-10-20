# EMA Hourly Continuation — SUSHI/USDT P50_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5009 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.8255 |
| gross_win_rate | 0.4488 |
| sharpe_ratio | -5.7584 |
| sortino_ratio | -2.0494 |
| max_drawdown | 0.9224 |
| cagr | -0.6348 |
| net_avg_win | 33.1375 |
| net_avg_loss | -50.5691 |
| avg_hold_time_bars | 6.2484 |
| exposure | 0.1821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
