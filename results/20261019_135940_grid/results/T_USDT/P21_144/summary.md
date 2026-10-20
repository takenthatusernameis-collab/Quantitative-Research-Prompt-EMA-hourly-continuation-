# EMA Hourly Continuation — T/USDT P21_144

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6594 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -3.0133 |
| sortino_ratio | -0.9185 |
| max_drawdown | 0.6742 |
| cagr | -0.3550 |
| net_avg_win | 57.0627 |
| net_avg_loss | -80.5108 |
| avg_hold_time_bars | 23.2123 |
| exposure | 0.4948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
