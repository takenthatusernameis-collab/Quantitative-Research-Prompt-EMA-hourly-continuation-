# EMA Hourly Continuation — XAI/USDT P20_200

**Symbol:** XAI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.8594 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9985 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.7052 |
| sortino_ratio | -0.1511 |
| max_drawdown | 0.2963 |
| cagr | -0.0689 |
| net_avg_win | 89.5041 |
| net_avg_loss | -104.1505 |
| avg_hold_time_bars | 73.3036 |
| exposure | 0.7464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
