# EMA Hourly Continuation — BICO/USDT P8_34

**Symbol:** BICO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1273 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8643 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -6.8880 |
| sortino_ratio | -3.4717 |
| max_drawdown | 0.9842 |
| cagr | -0.8074 |
| net_avg_win | 18.7037 |
| net_avg_loss | -29.6439 |
| avg_hold_time_bars | 6.0283 |
| exposure | 0.3488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
