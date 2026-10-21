# EMA Hourly Continuation — PEPE/USDT P21_34

**Symbol:** PEPE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6663 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -1.9945 |
| sortino_ratio | -0.4315 |
| max_drawdown | 0.3973 |
| cagr | -0.1796 |
| net_avg_win | 73.1169 |
| net_avg_loss | -95.4571 |
| avg_hold_time_bars | 5.3696 |
| exposure | 0.0561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
