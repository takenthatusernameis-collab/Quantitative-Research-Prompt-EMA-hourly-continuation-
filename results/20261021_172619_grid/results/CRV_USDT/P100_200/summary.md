# EMA Hourly Continuation — CRV/USDT P100_200

**Symbol:** CRV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8820 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -1.9506 |
| sortino_ratio | -0.4792 |
| max_drawdown | 0.4646 |
| cagr | -0.1984 |
| net_avg_win | 74.0718 |
| net_avg_loss | -91.5570 |
| avg_hold_time_bars | 9.6644 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
