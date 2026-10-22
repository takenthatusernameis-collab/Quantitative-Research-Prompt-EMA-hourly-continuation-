# EMA Hourly Continuation — GRT/USDT P50_55

**Symbol:** GRT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 787 |
| net_profit_factor | 0.2401 |
| net_win_rate | 0.3621 |
| gross_profit_factor | 0.6957 |
| gross_win_rate | 0.4269 |
| sharpe_ratio | -11.7788 |
| sortino_ratio | -4.8321 |
| max_drawdown | 0.9987 |
| cagr | -0.9273 |
| net_avg_win | 11.0702 |
| net_avg_loss | -26.1784 |
| avg_hold_time_bars | 1.9530 |
| exposure | 0.0696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
