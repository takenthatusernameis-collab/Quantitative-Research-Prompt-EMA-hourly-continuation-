# EMA Hourly Continuation — POPCAT/USDT P20_26

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1063 |
| net_profit_factor | 0.3807 |
| net_win_rate | 0.3603 |
| gross_profit_factor | 0.6594 |
| gross_win_rate | 0.3904 |
| sharpe_ratio | -12.9047 |
| sortino_ratio | -6.4699 |
| max_drawdown | 0.9992 |
| cagr | -0.9636 |
| net_avg_win | 16.0353 |
| net_avg_loss | -23.7261 |
| avg_hold_time_bars | 2.0715 |
| exposure | 0.1163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
