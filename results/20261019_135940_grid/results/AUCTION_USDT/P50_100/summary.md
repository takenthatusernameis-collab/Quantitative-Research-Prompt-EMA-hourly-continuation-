# EMA Hourly Continuation — AUCTION/USDT P50_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.4949 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -6.3288 |
| sortino_ratio | -2.2746 |
| max_drawdown | 0.9428 |
| cagr | -0.6712 |
| net_avg_win | 32.6473 |
| net_avg_loss | -50.4115 |
| avg_hold_time_bars | 6.8587 |
| exposure | 0.2021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
