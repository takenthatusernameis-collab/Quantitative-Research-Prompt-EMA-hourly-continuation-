# EMA Hourly Continuation — ILV/USDT P100_200

**Symbol:** ILV/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6328 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9791 |
| gross_win_rate | 0.5029 |
| sharpe_ratio | -2.4676 |
| sortino_ratio | -0.6410 |
| max_drawdown | 0.5391 |
| cagr | -0.2643 |
| net_avg_win | 56.1104 |
| net_avg_loss | -83.6090 |
| avg_hold_time_bars | 11.3647 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
