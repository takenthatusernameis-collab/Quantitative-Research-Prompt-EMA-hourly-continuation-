# EMA Hourly Continuation — CWEB/USDT P34_50

**Symbol:** CWEB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 859 |
| net_profit_factor | 0.2762 |
| net_win_rate | 0.2619 |
| gross_profit_factor | 0.7093 |
| gross_win_rate | 0.2875 |
| sharpe_ratio | -15.2319 |
| sortino_ratio | -6.7041 |
| max_drawdown | 0.9999 |
| cagr | -0.9766 |
| net_avg_win | 16.9596 |
| net_avg_loss | -21.7904 |
| avg_hold_time_bars | 3.7031 |
| exposure | 0.1446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
