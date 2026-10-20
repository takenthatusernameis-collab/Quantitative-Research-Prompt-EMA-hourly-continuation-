# EMA Hourly Continuation — EUL/USDT P34_200

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.5171 |
| net_win_rate | 0.4224 |
| gross_profit_factor | 0.7068 |
| gross_win_rate | 0.4224 |
| sharpe_ratio | -3.9305 |
| sortino_ratio | -1.1213 |
| max_drawdown | 0.7478 |
| cagr | -0.4177 |
| net_avg_win | 44.9444 |
| net_avg_loss | -63.5680 |
| avg_hold_time_bars | 21.9642 |
| exposure | 0.4183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
