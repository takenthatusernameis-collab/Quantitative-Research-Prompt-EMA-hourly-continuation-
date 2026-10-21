# EMA Hourly Continuation — TWT/USDT P20_34

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6881 |
| net_win_rate | 0.5370 |
| gross_profit_factor | 1.1052 |
| gross_win_rate | 0.5370 |
| sharpe_ratio | -1.9937 |
| sortino_ratio | -0.5620 |
| max_drawdown | 0.4922 |
| cagr | -0.2245 |
| net_avg_win | 51.2818 |
| net_avg_loss | -86.4550 |
| avg_hold_time_bars | 5.4021 |
| exposure | 0.0928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
