# EMA Hourly Continuation — XLM/USDT P20_100

**Symbol:** XLM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5113 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9939 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -4.4392 |
| sortino_ratio | -1.5691 |
| max_drawdown | 0.8663 |
| cagr | -0.5425 |
| net_avg_win | 28.4572 |
| net_avg_loss | -53.6255 |
| avg_hold_time_bars | 15.3587 |
| exposure | 0.4496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
