# EMA Hourly Continuation — ONDO/USDT P55_100

**Symbol:** ONDO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.4722 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.7785 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -6.2279 |
| sortino_ratio | -2.2055 |
| max_drawdown | 0.9312 |
| cagr | -0.6523 |
| net_avg_win | 31.8587 |
| net_avg_loss | -48.2481 |
| avg_hold_time_bars | 5.0272 |
| exposure | 0.1430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
