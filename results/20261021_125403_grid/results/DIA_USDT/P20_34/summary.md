# EMA Hourly Continuation — DIA/USDT P20_34

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6155 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 0.8967 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -3.2002 |
| sortino_ratio | -0.9762 |
| max_drawdown | 0.6909 |
| cagr | -0.3601 |
| net_avg_win | 49.8433 |
| net_avg_loss | -73.8399 |
| avg_hold_time_bars | 5.3538 |
| exposure | 0.1102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
