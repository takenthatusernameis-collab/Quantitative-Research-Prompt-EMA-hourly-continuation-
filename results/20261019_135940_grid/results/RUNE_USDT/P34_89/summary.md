# EMA Hourly Continuation — RUNE/USDT P34_89

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5857 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -4.1299 |
| sortino_ratio | -1.4813 |
| max_drawdown | 0.8469 |
| cagr | -0.5070 |
| net_avg_win | 37.1606 |
| net_avg_loss | -61.1281 |
| avg_hold_time_bars | 8.6196 |
| exposure | 0.2523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
