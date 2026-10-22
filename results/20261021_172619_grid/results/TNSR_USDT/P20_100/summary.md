# EMA Hourly Continuation — TNSR/USDT P20_100

**Symbol:** TNSR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.8179 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0024 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -1.4539 |
| sortino_ratio | -0.4653 |
| max_drawdown | 0.4768 |
| cagr | -0.1944 |
| net_avg_win | 74.9448 |
| net_avg_loss | -92.3583 |
| avg_hold_time_bars | 18.6653 |
| exposure | 0.4240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
