# EMA Hourly Continuation — SYN/USDT P12_20

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6840 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.9376 |
| gross_win_rate | 0.4782 |
| sharpe_ratio | -2.6533 |
| sortino_ratio | -0.7916 |
| max_drawdown | 0.6130 |
| cagr | -0.3048 |
| net_avg_win | 62.3137 |
| net_avg_loss | -83.4738 |
| avg_hold_time_bars | 4.9609 |
| exposure | 0.0981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
