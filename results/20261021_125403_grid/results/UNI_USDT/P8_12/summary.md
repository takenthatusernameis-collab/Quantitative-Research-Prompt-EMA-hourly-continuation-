# EMA Hourly Continuation — UNI/USDT P8_12

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 187 |
| net_profit_factor | 0.6406 |
| net_win_rate | 0.4759 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4759 |
| sharpe_ratio | -1.7836 |
| sortino_ratio | -0.3491 |
| max_drawdown | 0.3623 |
| cagr | -0.1479 |
| net_avg_win | 66.2940 |
| net_avg_loss | -93.9842 |
| avg_hold_time_bars | 4.9037 |
| exposure | 0.0417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
