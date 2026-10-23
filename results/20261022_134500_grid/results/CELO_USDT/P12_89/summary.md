# EMA Hourly Continuation — CELO/USDT P12_89

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0571 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -2.9255 |
| sortino_ratio | -1.0615 |
| max_drawdown | 0.7356 |
| cagr | -0.3992 |
| net_avg_win | 58.9603 |
| net_avg_loss | -79.7890 |
| avg_hold_time_bars | 18.4551 |
| exposure | 0.5579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
