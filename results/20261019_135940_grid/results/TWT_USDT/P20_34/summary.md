# EMA Hourly Continuation — TWT/USDT P20_34

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1219 |
| net_profit_factor | 0.2776 |
| net_win_rate | 0.4126 |
| gross_profit_factor | 0.7684 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -12.1791 |
| sortino_ratio | -6.0752 |
| max_drawdown | 0.9997 |
| cagr | -0.9574 |
| net_avg_win | 7.6365 |
| net_avg_loss | -19.3262 |
| avg_hold_time_bars | 2.7875 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
