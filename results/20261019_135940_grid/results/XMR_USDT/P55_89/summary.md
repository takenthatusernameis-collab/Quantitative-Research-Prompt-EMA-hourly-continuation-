# EMA Hourly Continuation — XMR/USDT P55_89

**Symbol:** XMR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.2549 |
| net_win_rate | 0.3826 |
| gross_profit_factor | 0.6710 |
| gross_win_rate | 0.3956 |
| sharpe_ratio | -11.8081 |
| sortino_ratio | -5.3953 |
| max_drawdown | 0.9990 |
| cagr | -0.9363 |
| net_avg_win | 8.9213 |
| net_avg_loss | -21.6940 |
| avg_hold_time_bars | 2.7982 |
| exposure | 0.1273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
