# EMA Hourly Continuation — KNC/USDT P20_55

**Symbol:** KNC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4743 |
| gross_profit_factor | 0.9699 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -3.8854 |
| sortino_ratio | -1.3861 |
| max_drawdown | 0.8116 |
| cagr | -0.4710 |
| net_avg_win | 53.3737 |
| net_avg_loss | -72.5533 |
| avg_hold_time_bars | 9.6576 |
| exposure | 0.2730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
