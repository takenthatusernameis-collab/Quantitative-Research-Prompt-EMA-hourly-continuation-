# EMA Hourly Continuation — MEME/USDT P12_26

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6154 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8247 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -3.8003 |
| sortino_ratio | -1.2751 |
| max_drawdown | 0.7747 |
| cagr | -0.4433 |
| net_avg_win | 49.2970 |
| net_avg_loss | -65.6630 |
| avg_hold_time_bars | 5.4036 |
| exposure | 0.1363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
