# EMA Hourly Continuation — TWT/USDT P26_50

**Symbol:** TWT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 992 |
| net_profit_factor | 0.3309 |
| net_win_rate | 0.4284 |
| gross_profit_factor | 0.7592 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -9.4052 |
| sortino_ratio | -4.1992 |
| max_drawdown | 0.9955 |
| cagr | -0.8814 |
| net_avg_win | 11.5792 |
| net_avg_loss | -26.2325 |
| avg_hold_time_bars | 3.7883 |
| exposure | 0.1708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
