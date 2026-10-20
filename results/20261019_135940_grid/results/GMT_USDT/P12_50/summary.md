# EMA Hourly Continuation — GMT/USDT P12_50

**Symbol:** GMT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.5303 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8716 |
| gross_win_rate | 0.4587 |
| sharpe_ratio | -7.2750 |
| sortino_ratio | -3.3988 |
| max_drawdown | 0.9854 |
| cagr | -0.8120 |
| net_avg_win | 22.2442 |
| net_avg_loss | -34.1558 |
| avg_hold_time_bars | 6.9515 |
| exposure | 0.3520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
