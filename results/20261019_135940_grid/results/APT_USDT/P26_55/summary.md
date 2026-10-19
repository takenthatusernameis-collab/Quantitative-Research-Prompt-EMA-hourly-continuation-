# EMA Hourly Continuation — APT/USDT P26_55

**Symbol:** APT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 968 |
| net_profit_factor | 0.4863 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4576 |
| sharpe_ratio | -7.6292 |
| sortino_ratio | -3.3535 |
| max_drawdown | 0.9857 |
| cagr | -0.8096 |
| net_avg_win | 21.3746 |
| net_avg_loss | -36.0228 |
| avg_hold_time_bars | 4.0486 |
| exposure | 0.1781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
