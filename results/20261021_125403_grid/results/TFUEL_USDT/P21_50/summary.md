# EMA Hourly Continuation — TFUEL/USDT P21_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.5381 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7689 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -5.0228 |
| sortino_ratio | -1.6480 |
| max_drawdown | 0.8561 |
| cagr | -0.5330 |
| net_avg_win | 44.5887 |
| net_avg_loss | -59.6071 |
| avg_hold_time_bars | 7.3171 |
| exposure | 0.1765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
