# EMA Hourly Continuation — GRAM/USDT P8_89

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9570 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.0530 |
| sortino_ratio | -0.6562 |
| max_drawdown | 0.5664 |
| cagr | -0.2607 |
| net_avg_win | 58.2546 |
| net_avg_loss | -77.8843 |
| avg_hold_time_bars | 26.7220 |
| exposure | 0.6073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
