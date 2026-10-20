# EMA Hourly Continuation — ETN/USDT P20_55

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.3330 |
| net_win_rate | 0.3512 |
| gross_profit_factor | 0.5218 |
| gross_win_rate | 0.3652 |
| sharpe_ratio | -11.1162 |
| sortino_ratio | -5.0160 |
| max_drawdown | 0.9951 |
| cagr | -0.9201 |
| net_avg_win | 16.5026 |
| net_avg_loss | -26.8307 |
| avg_hold_time_bars | 5.4854 |
| exposure | 0.2554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
