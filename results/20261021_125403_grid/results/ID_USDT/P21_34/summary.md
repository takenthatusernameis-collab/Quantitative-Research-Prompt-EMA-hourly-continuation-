# EMA Hourly Continuation — ID/USDT P21_34

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.6144 |
| net_win_rate | 0.4817 |
| gross_profit_factor | 0.9434 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -3.3363 |
| sortino_ratio | -1.0307 |
| max_drawdown | 0.6991 |
| cagr | -0.3753 |
| net_avg_win | 49.4172 |
| net_avg_loss | -74.7596 |
| avg_hold_time_bars | 5.5484 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
