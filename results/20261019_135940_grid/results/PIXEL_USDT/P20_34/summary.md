# EMA Hourly Continuation — PIXEL/USDT P20_34

**Symbol:** PIXEL/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1126 |
| net_profit_factor | 0.4499 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -8.6844 |
| sortino_ratio | -4.1107 |
| max_drawdown | 0.9939 |
| cagr | -0.8673 |
| net_avg_win | 16.4869 |
| net_avg_loss | -28.5415 |
| avg_hold_time_bars | 3.3908 |
| exposure | 0.1728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
