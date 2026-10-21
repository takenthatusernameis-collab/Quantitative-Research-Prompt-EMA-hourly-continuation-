# EMA Hourly Continuation — BNB/USDT P26_89

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6447 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0667 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -2.8691 |
| sortino_ratio | -0.8718 |
| max_drawdown | 0.6435 |
| cagr | -0.3277 |
| net_avg_win | 49.7911 |
| net_avg_loss | -82.6153 |
| avg_hold_time_bars | 13.9303 |
| exposure | 0.2818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
