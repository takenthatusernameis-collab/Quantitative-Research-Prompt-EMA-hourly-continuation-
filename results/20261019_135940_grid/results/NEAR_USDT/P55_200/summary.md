# EMA Hourly Continuation — NEAR/USDT P55_200

**Symbol:** NEAR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7438 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0326 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -1.8043 |
| sortino_ratio | -0.4975 |
| max_drawdown | 0.4628 |
| cagr | -0.2098 |
| net_avg_win | 67.1805 |
| net_avg_loss | -93.7135 |
| avg_hold_time_bars | 19.0501 |
| exposure | 0.3282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
