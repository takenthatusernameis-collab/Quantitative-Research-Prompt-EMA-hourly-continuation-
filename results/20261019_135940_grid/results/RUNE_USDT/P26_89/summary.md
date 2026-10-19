# EMA Hourly Continuation — RUNE/USDT P26_89

**Symbol:** RUNE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.5985 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -3.6538 |
| sortino_ratio | -1.2171 |
| max_drawdown | 0.7918 |
| cagr | -0.4488 |
| net_avg_win | 41.1551 |
| net_avg_loss | -67.5654 |
| avg_hold_time_bars | 15.9083 |
| exposure | 0.4100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
