# EMA Hourly Continuation — MEME/USDT P12_50

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.7189 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9071 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.9871 |
| sortino_ratio | -1.0959 |
| max_drawdown | 0.7364 |
| cagr | -0.3958 |
| net_avg_win | 58.8302 |
| net_avg_loss | -72.7457 |
| avg_hold_time_bars | 11.6139 |
| exposure | 0.3500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
