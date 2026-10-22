# EMA Hourly Continuation — POKT/USDT P8_55

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 745 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4403 |
| sharpe_ratio | -4.1134 |
| sortino_ratio | -1.5850 |
| max_drawdown | 0.8451 |
| cagr | -0.5193 |
| net_avg_win | 50.7839 |
| net_avg_loss | -59.8815 |
| avg_hold_time_bars | 11.9758 |
| exposure | 0.4037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
