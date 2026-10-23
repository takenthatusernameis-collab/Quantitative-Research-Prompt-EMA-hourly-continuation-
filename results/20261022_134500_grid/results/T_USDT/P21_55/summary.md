# EMA Hourly Continuation — T/USDT P21_55

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.5343 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9630 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -6.0854 |
| sortino_ratio | -2.3604 |
| max_drawdown | 0.9476 |
| cagr | -0.6883 |
| net_avg_win | 30.6141 |
| net_avg_loss | -49.2487 |
| avg_hold_time_bars | 7.0833 |
| exposure | 0.2462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
