# EMA Hourly Continuation — ZBCN/USDT P20_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.4280 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4551 |
| sharpe_ratio | -8.8829 |
| sortino_ratio | -4.3569 |
| max_drawdown | 0.9958 |
| cagr | -0.8903 |
| net_avg_win | 13.8981 |
| net_avg_loss | -26.1359 |
| avg_hold_time_bars | 2.4376 |
| exposure | 0.1356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
