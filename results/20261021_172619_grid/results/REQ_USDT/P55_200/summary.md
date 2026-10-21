# EMA Hourly Continuation — REQ/USDT P55_200

**Symbol:** REQ/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5629 |
| net_win_rate | 0.4206 |
| gross_profit_factor | 0.7954 |
| gross_win_rate | 0.4233 |
| sharpe_ratio | -4.0460 |
| sortino_ratio | -1.1188 |
| max_drawdown | 0.7491 |
| cagr | -0.4053 |
| net_avg_win | 59.0257 |
| net_avg_loss | -76.1335 |
| avg_hold_time_bars | 17.5053 |
| exposure | 0.3008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
