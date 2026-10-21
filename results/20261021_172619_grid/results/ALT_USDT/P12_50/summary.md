# EMA Hourly Continuation — ALT/USDT P12_50

**Symbol:** ALT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6992 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8827 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -3.3773 |
| sortino_ratio | -1.2583 |
| max_drawdown | 0.7887 |
| cagr | -0.4399 |
| net_avg_win | 56.4102 |
| net_avg_loss | -68.5312 |
| avg_hold_time_bars | 11.3561 |
| exposure | 0.3551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
