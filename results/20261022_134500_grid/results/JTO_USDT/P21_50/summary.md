# EMA Hourly Continuation — JTO/USDT P21_50

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.6064 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9888 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -5.1768 |
| sortino_ratio | -2.2613 |
| max_drawdown | 0.9373 |
| cagr | -0.6636 |
| net_avg_win | 31.0487 |
| net_avg_loss | -47.4217 |
| avg_hold_time_bars | 5.2425 |
| exposure | 0.2300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
