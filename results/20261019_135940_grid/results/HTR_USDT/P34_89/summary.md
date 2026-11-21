# EMA Hourly Continuation — HTR/USDT P34_89

**Symbol:** HTR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.4751 |
| net_win_rate | 0.4074 |
| gross_profit_factor | 0.7425 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -6.8582 |
| sortino_ratio | -2.6072 |
| max_drawdown | 0.9622 |
| cagr | -0.7223 |
| net_avg_win | 29.0642 |
| net_avg_loss | -42.0453 |
| avg_hold_time_bars | 7.9319 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
