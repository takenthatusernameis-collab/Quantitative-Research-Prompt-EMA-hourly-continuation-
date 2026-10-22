# EMA Hourly Continuation — ETN/USDT P12_26

**Symbol:** ETN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.4500 |
| net_win_rate | 0.3882 |
| gross_profit_factor | 0.6076 |
| gross_win_rate | 0.3882 |
| sharpe_ratio | -4.7776 |
| sortino_ratio | -1.3621 |
| max_drawdown | 0.7406 |
| cagr | -0.4714 |
| net_avg_win | 45.7529 |
| net_avg_loss | -64.5217 |
| avg_hold_time_bars | 6.3471 |
| exposure | 0.1172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
