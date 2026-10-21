# EMA Hourly Continuation — METIS/USDT P20_55

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9772 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.2286 |
| sortino_ratio | -0.7478 |
| max_drawdown | 0.6328 |
| cagr | -0.2907 |
| net_avg_win | 65.5462 |
| net_avg_loss | -83.8437 |
| avg_hold_time_bars | 8.3709 |
| exposure | 0.2093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
