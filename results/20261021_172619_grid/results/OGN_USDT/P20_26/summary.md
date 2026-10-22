# EMA Hourly Continuation — OGN/USDT P20_26

**Symbol:** OGN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.4993 |
| net_win_rate | 0.4364 |
| gross_profit_factor | 0.8044 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -3.8832 |
| sortino_ratio | -0.9493 |
| max_drawdown | 0.6758 |
| cagr | -0.3572 |
| net_avg_win | 52.7747 |
| net_avg_loss | -81.8450 |
| avg_hold_time_bars | 5.3746 |
| exposure | 0.0708 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
