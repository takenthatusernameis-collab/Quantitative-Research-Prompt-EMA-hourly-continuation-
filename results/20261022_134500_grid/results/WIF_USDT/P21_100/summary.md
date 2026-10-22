# EMA Hourly Continuation — WIF/USDT P21_100

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6533 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -3.8211 |
| sortino_ratio | -1.4046 |
| max_drawdown | 0.8187 |
| cagr | -0.4915 |
| net_avg_win | 47.3613 |
| net_avg_loss | -65.0890 |
| avg_hold_time_bars | 12.5604 |
| exposure | 0.3922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
