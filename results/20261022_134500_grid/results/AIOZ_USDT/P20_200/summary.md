# EMA Hourly Continuation — AIOZ/USDT P20_200

**Symbol:** AIOZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6628 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.8941 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -2.8916 |
| sortino_ratio | -0.8889 |
| max_drawdown | 0.6982 |
| cagr | -0.3409 |
| net_avg_win | 56.9561 |
| net_avg_loss | -77.9277 |
| avg_hold_time_bars | 28.8365 |
| exposure | 0.6174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
