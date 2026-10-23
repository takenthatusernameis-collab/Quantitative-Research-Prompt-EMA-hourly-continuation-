# EMA Hourly Continuation — MEME/USDT P21_89

**Symbol:** MEME/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.6373 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -4.0755 |
| sortino_ratio | -1.5101 |
| max_drawdown | 0.8544 |
| cagr | -0.5169 |
| net_avg_win | 45.0856 |
| net_avg_loss | -62.8651 |
| avg_hold_time_bars | 12.9698 |
| exposure | 0.4097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
