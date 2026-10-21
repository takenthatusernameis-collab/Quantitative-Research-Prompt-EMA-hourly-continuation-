# EMA Hourly Continuation — RUNE/USDT P8_12

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.5865 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -2.5096 |
| sortino_ratio | -0.5375 |
| max_drawdown | 0.4660 |
| cagr | -0.2183 |
| net_avg_win | 62.9027 |
| net_avg_loss | -92.9462 |
| avg_hold_time_bars | 4.2054 |
| exposure | 0.0428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
