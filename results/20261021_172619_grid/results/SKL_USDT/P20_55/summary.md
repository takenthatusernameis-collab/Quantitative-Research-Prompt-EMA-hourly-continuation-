# EMA Hourly Continuation — SKL/USDT P20_55

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.8991 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -2.9117 |
| sortino_ratio | -0.9684 |
| max_drawdown | 0.6898 |
| cagr | -0.3587 |
| net_avg_win | 59.0904 |
| net_avg_loss | -75.4010 |
| avg_hold_time_bars | 8.4835 |
| exposure | 0.2098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
