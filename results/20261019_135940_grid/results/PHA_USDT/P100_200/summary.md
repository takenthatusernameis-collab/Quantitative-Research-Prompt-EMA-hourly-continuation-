# EMA Hourly Continuation — PHA/USDT P100_200

**Symbol:** PHA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.5195 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7813 |
| gross_win_rate | 0.4397 |
| sharpe_ratio | -3.9802 |
| sortino_ratio | -1.1606 |
| max_drawdown | 0.7550 |
| cagr | -0.4190 |
| net_avg_win | 43.9709 |
| net_avg_loss | -64.5402 |
| avg_hold_time_bars | 7.8109 |
| exposure | 0.1502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
