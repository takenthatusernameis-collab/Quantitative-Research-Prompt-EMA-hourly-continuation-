# EMA Hourly Continuation — COMP/USDT P89_200

**Symbol:** COMP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.4458 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8353 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.4795 |
| sortino_ratio | -1.2849 |
| max_drawdown | 0.8049 |
| cagr | -0.4764 |
| net_avg_win | 33.6503 |
| net_avg_loss | -63.0053 |
| avg_hold_time_bars | 9.7654 |
| exposure | 0.1873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
