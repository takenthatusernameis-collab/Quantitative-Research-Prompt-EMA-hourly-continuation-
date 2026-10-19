# EMA Hourly Continuation — LINK/USDT P34_55

**Symbol:** LINK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 827 |
| net_profit_factor | 0.4527 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.9379 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -7.8508 |
| sortino_ratio | -3.2037 |
| max_drawdown | 0.9822 |
| cagr | -0.7990 |
| net_avg_win | 21.4343 |
| net_avg_loss | -40.0572 |
| avg_hold_time_bars | 3.1657 |
| exposure | 0.1190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
