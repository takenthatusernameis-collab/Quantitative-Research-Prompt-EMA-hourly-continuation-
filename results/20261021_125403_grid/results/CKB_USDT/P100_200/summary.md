# EMA Hourly Continuation — CKB/USDT P100_200

**Symbol:** CKB/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0126 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -1.2739 |
| sortino_ratio | -0.3089 |
| max_drawdown | 0.3058 |
| cagr | -0.1331 |
| net_avg_win | 73.1121 |
| net_avg_loss | -96.5601 |
| avg_hold_time_bars | 12.2413 |
| exposure | 0.1591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
