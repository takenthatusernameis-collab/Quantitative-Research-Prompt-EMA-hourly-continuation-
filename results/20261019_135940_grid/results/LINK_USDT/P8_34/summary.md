# EMA Hourly Continuation — LINK/USDT P8_34

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1365 |
| net_profit_factor | 0.4880 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.9435 |
| gross_win_rate | 0.4696 |
| sharpe_ratio | -9.0414 |
| sortino_ratio | -4.6852 |
| max_drawdown | 0.9973 |
| cagr | -0.9041 |
| net_avg_win | 15.3325 |
| net_avg_loss | -26.1455 |
| avg_hold_time_bars | 5.1890 |
| exposure | 0.3220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
