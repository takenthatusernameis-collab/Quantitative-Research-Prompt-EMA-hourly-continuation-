# EMA Hourly Continuation — EDU/USDT P21_100

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 717 |
| net_profit_factor | 0.6012 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -3.7654 |
| sortino_ratio | -1.4220 |
| max_drawdown | 0.8220 |
| cagr | -0.4886 |
| net_avg_win | 36.3842 |
| net_avg_loss | -53.9741 |
| avg_hold_time_bars | 12.4240 |
| exposure | 0.4031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
