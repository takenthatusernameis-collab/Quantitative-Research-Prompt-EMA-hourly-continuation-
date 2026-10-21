# EMA Hourly Continuation — DBR/USDT P12_34

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5459 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8406 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -4.6720 |
| sortino_ratio | -1.5826 |
| max_drawdown | 0.7894 |
| cagr | -0.5197 |
| net_avg_win | 45.8621 |
| net_avg_loss | -67.6073 |
| avg_hold_time_bars | 8.6667 |
| exposure | 0.2233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
