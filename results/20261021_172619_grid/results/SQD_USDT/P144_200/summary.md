# EMA Hourly Continuation — SQD/USDT P144_200

**Symbol:** SQD/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.9106 |
| net_win_rate | 0.5317 |
| gross_profit_factor | 1.1294 |
| gross_win_rate | 0.5317 |
| sharpe_ratio | -0.3988 |
| sortino_ratio | -0.0839 |
| max_drawdown | 0.1864 |
| cagr | -0.0399 |
| net_avg_win | 87.9287 |
| net_avg_loss | -109.6373 |
| avg_hold_time_bars | 7.6049 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
