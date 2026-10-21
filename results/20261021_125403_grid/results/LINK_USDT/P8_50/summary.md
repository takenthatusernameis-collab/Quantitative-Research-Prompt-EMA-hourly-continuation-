# EMA Hourly Continuation — LINK/USDT P8_50

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.7686 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9816 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -2.4097 |
| sortino_ratio | -0.8740 |
| max_drawdown | 0.6689 |
| cagr | -0.3316 |
| net_avg_win | 67.0891 |
| net_avg_loss | -83.5770 |
| avg_hold_time_bars | 14.0559 |
| exposure | 0.4115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
