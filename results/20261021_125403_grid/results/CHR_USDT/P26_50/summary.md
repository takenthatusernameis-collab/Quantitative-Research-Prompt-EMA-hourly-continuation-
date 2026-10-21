# EMA Hourly Continuation — CHR/USDT P26_50

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.6987 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9381 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.5389 |
| sortino_ratio | -0.8064 |
| max_drawdown | 0.6183 |
| cagr | -0.3079 |
| net_avg_win | 58.6777 |
| net_avg_loss | -78.4064 |
| avg_hold_time_bars | 5.9677 |
| exposure | 0.1337 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
