# EMA Hourly Continuation — SSV/USDT P8_100

**Symbol:** SSV/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7724 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -1.7149 |
| sortino_ratio | -0.4981 |
| max_drawdown | 0.4936 |
| cagr | -0.2057 |
| net_avg_win | 75.1213 |
| net_avg_loss | -87.9775 |
| avg_hold_time_bars | 37.7709 |
| exposure | 0.7161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
