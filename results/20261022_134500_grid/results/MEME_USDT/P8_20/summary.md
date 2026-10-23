# EMA Hourly Continuation — MEME/USDT P8_20

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1657 |
| net_profit_factor | 0.4287 |
| net_win_rate | 0.4303 |
| gross_profit_factor | 0.8840 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -11.0946 |
| sortino_ratio | -6.3801 |
| max_drawdown | 0.9996 |
| cagr | -0.9569 |
| net_avg_win | 10.5216 |
| net_avg_loss | -18.5363 |
| avg_hold_time_bars | 2.8847 |
| exposure | 0.2173 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
