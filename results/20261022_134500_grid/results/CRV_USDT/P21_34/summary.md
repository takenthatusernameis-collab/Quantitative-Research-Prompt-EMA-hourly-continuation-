# EMA Hourly Continuation — CRV/USDT P21_34

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1138 |
| net_profit_factor | 0.3812 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8398 |
| gross_win_rate | 0.4666 |
| sharpe_ratio | -9.4544 |
| sortino_ratio | -4.5131 |
| max_drawdown | 0.9968 |
| cagr | -0.8976 |
| net_avg_win | 12.1587 |
| net_avg_loss | -25.4462 |
| avg_hold_time_bars | 2.2531 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
