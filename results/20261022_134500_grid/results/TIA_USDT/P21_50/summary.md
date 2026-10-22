# EMA Hourly Continuation — TIA/USDT P21_50

**Symbol:** TIA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 1.0137 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -5.2236 |
| sortino_ratio | -2.3156 |
| max_drawdown | 0.9430 |
| cagr | -0.6715 |
| net_avg_win | 35.4977 |
| net_avg_loss | -51.6486 |
| avg_hold_time_bars | 4.4061 |
| exposure | 0.1983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
