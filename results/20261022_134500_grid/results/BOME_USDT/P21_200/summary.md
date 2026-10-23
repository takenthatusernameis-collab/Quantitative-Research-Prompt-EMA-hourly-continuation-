# EMA Hourly Continuation — BOME/USDT P21_200

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.6702 |
| net_win_rate | 0.4770 |
| gross_profit_factor | 0.8976 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -2.2323 |
| sortino_ratio | -0.5799 |
| max_drawdown | 0.5300 |
| cagr | -0.2446 |
| net_avg_win | 61.8904 |
| net_avg_loss | -84.2304 |
| avg_hold_time_bars | 40.6322 |
| exposure | 0.6427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
