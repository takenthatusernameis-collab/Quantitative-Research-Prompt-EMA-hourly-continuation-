# EMA Hourly Continuation — SYN/USDT P21_200

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.9560 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1096 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -0.1892 |
| sortino_ratio | -0.0480 |
| max_drawdown | 0.1961 |
| cagr | -0.0268 |
| net_avg_win | 87.9784 |
| net_avg_loss | -102.7449 |
| avg_hold_time_bars | 44.9515 |
| exposure | 0.6314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
