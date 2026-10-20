# EMA Hourly Continuation — PUFFER/USDT P12_21

**Symbol:** PUFFER/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1064 |
| net_profit_factor | 0.4691 |
| net_win_rate | 0.4267 |
| gross_profit_factor | 0.8601 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -10.0733 |
| sortino_ratio | -5.1583 |
| max_drawdown | 0.9947 |
| cagr | -0.9249 |
| net_avg_win | 19.3582 |
| net_avg_loss | -30.7126 |
| avg_hold_time_bars | 2.9765 |
| exposure | 0.1792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
