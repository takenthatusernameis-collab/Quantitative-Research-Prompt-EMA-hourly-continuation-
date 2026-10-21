# EMA Hourly Continuation — MEME/USDT P8_20

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.6625 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.8918 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -3.4715 |
| sortino_ratio | -1.2084 |
| max_drawdown | 0.7559 |
| cagr | -0.4256 |
| net_avg_win | 53.0621 |
| net_avg_loss | -70.2417 |
| avg_hold_time_bars | 5.2118 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
