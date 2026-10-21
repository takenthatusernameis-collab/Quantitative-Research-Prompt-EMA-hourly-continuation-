# EMA Hourly Continuation — ANYONE/USDT P144_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.7229 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.8919 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -1.4104 |
| sortino_ratio | -0.2910 |
| max_drawdown | 0.3171 |
| cagr | -0.1258 |
| net_avg_win | 75.9452 |
| net_avg_loss | -95.5024 |
| avg_hold_time_bars | 8.7672 |
| exposure | 0.0837 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
