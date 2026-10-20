# EMA Hourly Continuation — ETN/USDT P21_34

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.2316 |
| net_win_rate | 0.2896 |
| gross_profit_factor | 0.4190 |
| gross_win_rate | 0.3239 |
| sharpe_ratio | -15.5964 |
| sortino_ratio | -7.8342 |
| max_drawdown | 0.9998 |
| cagr | -0.9842 |
| net_avg_win | 10.1824 |
| net_avg_loss | -17.9234 |
| avg_hold_time_bars | 2.8669 |
| exposure | 0.1592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
