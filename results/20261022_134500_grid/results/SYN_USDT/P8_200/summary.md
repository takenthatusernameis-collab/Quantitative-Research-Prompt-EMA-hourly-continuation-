# EMA Hourly Continuation — SYN/USDT P8_200

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.6272 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8378 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -2.6957 |
| sortino_ratio | -0.7689 |
| max_drawdown | 0.6175 |
| cagr | -0.3093 |
| net_avg_win | 52.7473 |
| net_avg_loss | -72.4647 |
| avg_hold_time_bars | 41.4796 |
| exposure | 0.7862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
