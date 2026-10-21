# EMA Hourly Continuation — MEME/USDT P26_55

**Symbol:** MEME/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7169 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.6737 |
| sortino_ratio | -0.8539 |
| max_drawdown | 0.6738 |
| cagr | -0.3234 |
| net_avg_win | 65.9759 |
| net_avg_loss | -85.2724 |
| avg_hold_time_bars | 5.8838 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
