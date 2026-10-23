# EMA Hourly Continuation — MEW/USDT P21_89

**Symbol:** MEW/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.6024 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8704 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -4.2759 |
| sortino_ratio | -1.5942 |
| max_drawdown | 0.8560 |
| cagr | -0.5334 |
| net_avg_win | 39.3746 |
| net_avg_loss | -56.5720 |
| avg_hold_time_bars | 11.4158 |
| exposure | 0.3669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
