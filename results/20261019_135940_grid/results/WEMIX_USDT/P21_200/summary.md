# EMA Hourly Continuation — WEMIX/USDT P21_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.3733 |
| net_win_rate | 0.3250 |
| gross_profit_factor | 0.5620 |
| gross_win_rate | 0.3321 |
| sharpe_ratio | -8.1874 |
| sortino_ratio | -2.7232 |
| max_drawdown | 0.9672 |
| cagr | -0.7422 |
| net_avg_win | 31.8185 |
| net_avg_loss | -41.0286 |
| avg_hold_time_bars | 26.8061 |
| exposure | 0.6787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
