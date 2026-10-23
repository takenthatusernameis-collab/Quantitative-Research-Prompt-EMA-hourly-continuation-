# EMA Hourly Continuation — MEME/USDT P8_34

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1421 |
| net_profit_factor | 0.5402 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -7.3595 |
| sortino_ratio | -3.8993 |
| max_drawdown | 0.9915 |
| cagr | -0.8483 |
| net_avg_win | 17.6208 |
| net_avg_loss | -28.3678 |
| avg_hold_time_bars | 5.0106 |
| exposure | 0.3236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
