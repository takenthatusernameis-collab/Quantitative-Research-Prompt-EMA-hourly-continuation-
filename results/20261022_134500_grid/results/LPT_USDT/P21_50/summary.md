# EMA Hourly Continuation — LPT/USDT P21_50

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1073 |
| net_profit_factor | 0.4499 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7709 |
| gross_win_rate | 0.4390 |
| sharpe_ratio | -8.9527 |
| sortino_ratio | -4.1461 |
| max_drawdown | 0.9943 |
| cagr | -0.8685 |
| net_avg_win | 18.4324 |
| net_avg_loss | -28.5877 |
| avg_hold_time_bars | 4.3821 |
| exposure | 0.2137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
