# EMA Hourly Continuation — POPCAT/USDT P12_34

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1133 |
| net_profit_factor | 0.5591 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8126 |
| gross_win_rate | 0.4431 |
| sharpe_ratio | -8.1037 |
| sortino_ratio | -4.1516 |
| max_drawdown | 0.9866 |
| cagr | -0.8626 |
| net_avg_win | 25.7371 |
| net_avg_loss | -34.5767 |
| avg_hold_time_bars | 4.0644 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
