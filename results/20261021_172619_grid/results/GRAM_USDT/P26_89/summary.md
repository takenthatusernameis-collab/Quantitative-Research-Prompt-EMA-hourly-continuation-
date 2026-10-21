# EMA Hourly Continuation — GRAM/USDT P26_89

**Symbol:** GRAM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6697 |
| net_win_rate | 0.4747 |
| gross_profit_factor | 0.9113 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -2.6656 |
| sortino_ratio | -0.8122 |
| max_drawdown | 0.6270 |
| cagr | -0.3100 |
| net_avg_win | 56.8994 |
| net_avg_loss | -76.7883 |
| avg_hold_time_bars | 13.1033 |
| exposure | 0.2710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
