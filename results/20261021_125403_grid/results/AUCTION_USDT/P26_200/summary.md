# EMA Hourly Continuation — AUCTION/USDT P26_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6873 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9011 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.3994 |
| sortino_ratio | -0.6623 |
| max_drawdown | 0.5585 |
| cagr | -0.2687 |
| net_avg_win | 65.9192 |
| net_avg_loss | -85.9871 |
| avg_hold_time_bars | 31.3922 |
| exposure | 0.5470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
