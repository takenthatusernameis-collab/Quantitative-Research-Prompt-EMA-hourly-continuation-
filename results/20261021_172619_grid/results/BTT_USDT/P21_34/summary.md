# EMA Hourly Continuation — BTT/USDT P21_34

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 325 |
| net_profit_factor | 0.3937 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7428 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -5.8479 |
| sortino_ratio | -1.5412 |
| max_drawdown | 0.8409 |
| cagr | -0.5168 |
| net_avg_win | 41.9040 |
| net_avg_loss | -70.9617 |
| avg_hold_time_bars | 6.1077 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
