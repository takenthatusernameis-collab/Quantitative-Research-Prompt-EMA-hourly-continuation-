# EMA Hourly Continuation — ZIL/USDT P26_200

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.8609 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0655 |
| gross_win_rate | 0.5194 |
| sharpe_ratio | -0.7669 |
| sortino_ratio | -0.1938 |
| max_drawdown | 0.2640 |
| cagr | -0.0880 |
| net_avg_win | 79.4045 |
| net_avg_loss | -99.6648 |
| avg_hold_time_bars | 39.7484 |
| exposure | 0.5601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
