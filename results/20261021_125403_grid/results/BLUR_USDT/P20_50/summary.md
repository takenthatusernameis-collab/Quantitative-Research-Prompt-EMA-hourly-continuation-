# EMA Hourly Continuation — BLUR/USDT P20_50

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7808 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -1.8259 |
| sortino_ratio | -0.6248 |
| max_drawdown | 0.5892 |
| cagr | -0.2490 |
| net_avg_win | 62.7523 |
| net_avg_loss | -84.7196 |
| avg_hold_time_bars | 7.3761 |
| exposure | 0.1899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
