# EMA Hourly Continuation — THETA/USDT P21_50

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.6797 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -2.4801 |
| sortino_ratio | -0.7478 |
| max_drawdown | 0.5945 |
| cagr | -0.2893 |
| net_avg_win | 57.6517 |
| net_avg_loss | -77.1708 |
| avg_hold_time_bars | 7.4629 |
| exposure | 0.1510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
