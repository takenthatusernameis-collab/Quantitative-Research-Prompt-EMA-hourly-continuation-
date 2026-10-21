# EMA Hourly Continuation — MEME/USDT P8_100

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.8034 |
| net_win_rate | 0.4908 |
| gross_profit_factor | 0.9597 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -1.5113 |
| sortino_ratio | -0.4760 |
| max_drawdown | 0.4368 |
| cagr | -0.1983 |
| net_avg_win | 72.8475 |
| net_avg_loss | -87.3791 |
| avg_hold_time_bars | 29.5483 |
| exposure | 0.6541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
