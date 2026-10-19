# EMA Hourly Continuation — ZK/USDT P20_34

**Symbol:** ZK/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1122 |
| net_profit_factor | 0.5133 |
| net_win_rate | 0.4340 |
| gross_profit_factor | 0.9796 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -9.2704 |
| sortino_ratio | -4.5350 |
| max_drawdown | 0.9951 |
| cagr | -0.8961 |
| net_avg_win | 21.5476 |
| net_avg_loss | -32.1950 |
| avg_hold_time_bars | 2.7870 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
