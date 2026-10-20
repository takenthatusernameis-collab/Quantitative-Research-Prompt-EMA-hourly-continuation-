# EMA Hourly Continuation — DIA/USDT P34_50

**Symbol:** DIA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.3526 |
| net_win_rate | 0.4027 |
| gross_profit_factor | 0.7386 |
| gross_win_rate | 0.4300 |
| sharpe_ratio | -9.3463 |
| sortino_ratio | -3.9265 |
| max_drawdown | 0.9929 |
| cagr | -0.8592 |
| net_avg_win | 15.2752 |
| net_avg_loss | -29.2120 |
| avg_hold_time_bars | 3.3276 |
| exposure | 0.1324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
