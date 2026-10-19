# EMA Hourly Continuation — BONK/USDT P12_100

**Symbol:** BONK/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9991 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.9392 |
| sortino_ratio | -1.0379 |
| max_drawdown | 0.7445 |
| cagr | -0.3935 |
| net_avg_win | 56.4541 |
| net_avg_loss | -76.0878 |
| avg_hold_time_bars | 20.8218 |
| exposure | 0.6000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
