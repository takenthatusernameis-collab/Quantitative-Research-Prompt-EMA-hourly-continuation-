# EMA Hourly Continuation — EWT/USDT P100_200

**Symbol:** EWT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.4478 |
| gross_profit_factor | 0.8033 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -1.9684 |
| sortino_ratio | -0.4233 |
| max_drawdown | 0.4187 |
| cagr | -0.1779 |
| net_avg_win | 71.6727 |
| net_avg_loss | -88.7213 |
| avg_hold_time_bars | 13.3217 |
| exposure | 0.1393 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
