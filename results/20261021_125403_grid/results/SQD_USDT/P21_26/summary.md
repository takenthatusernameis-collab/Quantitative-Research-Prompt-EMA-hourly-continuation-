# EMA Hourly Continuation — SQD/USDT P21_26

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.7832 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0226 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -1.1373 |
| sortino_ratio | -0.2467 |
| max_drawdown | 0.2911 |
| cagr | -0.1074 |
| net_avg_win | 77.7689 |
| net_avg_loss | -102.0340 |
| avg_hold_time_bars | 4.8235 |
| exposure | 0.0501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
