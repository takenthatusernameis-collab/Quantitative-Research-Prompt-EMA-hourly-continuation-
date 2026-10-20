# EMA Hourly Continuation — SYN/USDT P34_50

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 923 |
| net_profit_factor | 0.4163 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8216 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -8.0144 |
| sortino_ratio | -3.4172 |
| max_drawdown | 0.9869 |
| cagr | -0.8212 |
| net_avg_win | 17.5956 |
| net_avg_loss | -32.3246 |
| avg_hold_time_bars | 3.2698 |
| exposure | 0.1372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
