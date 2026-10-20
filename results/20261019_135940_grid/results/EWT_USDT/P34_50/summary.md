# EMA Hourly Continuation — EWT/USDT P34_50

**Symbol:** EWT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.3226 |
| net_win_rate | 0.3827 |
| gross_profit_factor | 0.6892 |
| gross_win_rate | 0.3945 |
| sharpe_ratio | -9.9290 |
| sortino_ratio | -3.9038 |
| max_drawdown | 0.9940 |
| cagr | -0.8694 |
| net_avg_win | 16.2077 |
| net_avg_loss | -31.1516 |
| avg_hold_time_bars | 3.6658 |
| exposure | 0.1271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
