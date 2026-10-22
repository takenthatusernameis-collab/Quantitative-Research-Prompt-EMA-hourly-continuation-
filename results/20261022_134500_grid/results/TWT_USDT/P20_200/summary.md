# EMA Hourly Continuation — TWT/USDT P20_200

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6462 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9853 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.5547 |
| sortino_ratio | -0.7111 |
| max_drawdown | 0.6161 |
| cagr | -0.2911 |
| net_avg_win | 54.4731 |
| net_avg_loss | -80.9548 |
| avg_hold_time_bars | 35.9773 |
| exposure | 0.6476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
