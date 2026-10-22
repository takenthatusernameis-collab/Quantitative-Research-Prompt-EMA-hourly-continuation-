# EMA Hourly Continuation — SYN/USDT P12_34

**Symbol:** SYN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.7144 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -2.9488 |
| sortino_ratio | -1.0914 |
| max_drawdown | 0.7291 |
| cagr | -0.3951 |
| net_avg_win | 56.2155 |
| net_avg_loss | -70.7131 |
| avg_hold_time_bars | 6.8531 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
