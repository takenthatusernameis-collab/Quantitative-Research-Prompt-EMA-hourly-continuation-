# EMA Hourly Continuation — SNX/USDT P20_21

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1194 |
| net_profit_factor | 0.1562 |
| net_win_rate | 0.3157 |
| gross_profit_factor | 0.7230 |
| gross_win_rate | 0.4045 |
| sharpe_ratio | -16.8335 |
| sortino_ratio | -8.7357 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 4.9096 |
| net_avg_loss | -14.5053 |
| avg_hold_time_bars | 1.7211 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
