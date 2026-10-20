# EMA Hourly Continuation — CTC/USDT P26_55

**Symbol:** CTC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.4340 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -7.6037 |
| sortino_ratio | -3.2149 |
| max_drawdown | 0.9830 |
| cagr | -0.7992 |
| net_avg_win | 18.7813 |
| net_avg_loss | -34.7078 |
| avg_hold_time_bars | 4.9201 |
| exposure | 0.2015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
