# EMA Hourly Continuation — BICO/USDT P21_26

**Symbol:** BICO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1090 |
| net_profit_factor | 0.2551 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 0.7439 |
| gross_win_rate | 0.4321 |
| sharpe_ratio | -11.8439 |
| sortino_ratio | -5.6114 |
| max_drawdown | 0.9992 |
| cagr | -0.9415 |
| net_avg_win | 8.2080 |
| net_avg_loss | -19.9327 |
| avg_hold_time_bars | 2.6459 |
| exposure | 0.1311 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
