# EMA Hourly Continuation — JTO/USDT P12_21

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1488 |
| net_profit_factor | 0.3904 |
| net_win_rate | 0.4321 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -10.7450 |
| sortino_ratio | -5.8606 |
| max_drawdown | 0.9994 |
| cagr | -0.9456 |
| net_avg_win | 9.9536 |
| net_avg_loss | -19.4006 |
| avg_hold_time_bars | 2.5356 |
| exposure | 0.1715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
