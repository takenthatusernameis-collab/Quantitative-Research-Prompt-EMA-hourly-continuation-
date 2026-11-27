# EMA Hourly Continuation — SHR/USDT P34_55

**Symbol:** SHR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1070 |
| net_profit_factor | 0.3324 |
| net_win_rate | 0.3065 |
| gross_profit_factor | 0.5474 |
| gross_win_rate | 0.3140 |
| sharpe_ratio | -12.1340 |
| sortino_ratio | -5.5879 |
| max_drawdown | 0.9991 |
| cagr | -0.9377 |
| net_avg_win | 15.1632 |
| net_avg_loss | -20.1677 |
| avg_hold_time_bars | 3.2794 |
| exposure | 0.1588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
