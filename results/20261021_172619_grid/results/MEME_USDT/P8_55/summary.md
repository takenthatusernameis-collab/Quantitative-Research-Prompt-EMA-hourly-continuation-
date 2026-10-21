# EMA Hourly Continuation — MEME/USDT P8_55

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.7698 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9518 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -2.3593 |
| sortino_ratio | -0.8898 |
| max_drawdown | 0.6590 |
| cagr | -0.3366 |
| net_avg_win | 63.4559 |
| net_avg_loss | -77.8387 |
| avg_hold_time_bars | 14.5903 |
| exposure | 0.4629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
