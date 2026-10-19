# EMA Hourly Continuation — UNI/USDT P21_34

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1156 |
| net_profit_factor | 0.3309 |
| net_win_rate | 0.4014 |
| gross_profit_factor | 0.7944 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -11.8082 |
| sortino_ratio | -5.7067 |
| max_drawdown | 0.9995 |
| cagr | -0.9490 |
| net_avg_win | 10.6516 |
| net_avg_loss | -21.5848 |
| avg_hold_time_bars | 2.2292 |
| exposure | 0.1171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
