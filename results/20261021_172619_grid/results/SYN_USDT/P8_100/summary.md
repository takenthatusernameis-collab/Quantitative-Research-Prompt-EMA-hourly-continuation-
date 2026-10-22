# EMA Hourly Continuation — SYN/USDT P8_100

**Symbol:** SYN/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.9273 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0775 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.4636 |
| sortino_ratio | -0.1405 |
| max_drawdown | 0.2650 |
| cagr | -0.0684 |
| net_avg_win | 89.9909 |
| net_avg_loss | -105.2463 |
| avg_hold_time_bars | 33.4707 |
| exposure | 0.6755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
