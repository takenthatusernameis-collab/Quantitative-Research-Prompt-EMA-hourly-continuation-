# EMA Hourly Continuation — HTX/USDT P20_26

**Symbol:** HTX/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1367 |
| net_profit_factor | 0.0601 |
| net_win_rate | 0.1690 |
| gross_profit_factor | 0.3513 |
| gross_win_rate | 0.2868 |
| sharpe_ratio | -24.1527 |
| sortino_ratio | -14.9442 |
| max_drawdown | 1.0000 |
| cagr | -0.9997 |
| net_avg_win | 2.7692 |
| net_avg_loss | -9.3659 |
| avg_hold_time_bars | 2.4901 |
| exposure | 0.1540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
