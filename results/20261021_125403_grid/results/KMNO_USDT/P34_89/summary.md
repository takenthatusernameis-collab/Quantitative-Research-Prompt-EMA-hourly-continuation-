# EMA Hourly Continuation — KMNO/USDT P34_89

**Symbol:** KMNO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7353 |
| net_win_rate | 0.4855 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -1.8705 |
| sortino_ratio | -0.5237 |
| max_drawdown | 0.4865 |
| cagr | -0.2147 |
| net_avg_win | 67.9097 |
| net_avg_loss | -87.1513 |
| avg_hold_time_bars | 11.9947 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
