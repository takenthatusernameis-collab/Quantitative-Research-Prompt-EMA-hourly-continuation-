# EMA Hourly Continuation — T/USDT P21_34

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.3950 |
| net_win_rate | 0.4177 |
| gross_profit_factor | 0.9152 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -9.3518 |
| sortino_ratio | -3.9498 |
| max_drawdown | 0.9941 |
| cagr | -0.8685 |
| net_avg_win | 17.4009 |
| net_avg_loss | -31.5973 |
| avg_hold_time_bars | 4.1366 |
| exposure | 0.1672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
