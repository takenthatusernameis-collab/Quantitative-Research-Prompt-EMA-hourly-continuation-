# EMA Hourly Continuation — PIXEL/USDT P20_50

**Symbol:** PIXEL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.5659 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -5.6959 |
| sortino_ratio | -2.4889 |
| max_drawdown | 0.9535 |
| cagr | -0.7010 |
| net_avg_win | 27.1708 |
| net_avg_loss | -42.6873 |
| avg_hold_time_bars | 5.8023 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
