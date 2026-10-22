# EMA Hourly Continuation — XAI/USDT P26_55

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7816 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0289 |
| gross_win_rate | 0.5049 |
| sharpe_ratio | -1.9025 |
| sortino_ratio | -0.6173 |
| max_drawdown | 0.5395 |
| cagr | -0.2468 |
| net_avg_win | 70.6255 |
| net_avg_loss | -92.1469 |
| avg_hold_time_bars | 7.6067 |
| exposure | 0.1767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
