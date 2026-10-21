# EMA Hourly Continuation — KAS/USDT P50_89

**Symbol:** KAS/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.6376 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.2078 |
| sortino_ratio | -0.5377 |
| max_drawdown | 0.4603 |
| cagr | -0.2178 |
| net_avg_win | 59.1221 |
| net_avg_loss | -82.4882 |
| avg_hold_time_bars | 7.8385 |
| exposure | 0.1037 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
