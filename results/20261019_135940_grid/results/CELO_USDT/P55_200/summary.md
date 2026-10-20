# EMA Hourly Continuation — CELO/USDT P55_200

**Symbol:** CELO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7188 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0413 |
| gross_win_rate | 0.5066 |
| sharpe_ratio | -2.0177 |
| sortino_ratio | -0.5489 |
| max_drawdown | 0.5002 |
| cagr | -0.2333 |
| net_avg_win | 65.3560 |
| net_avg_loss | -92.3801 |
| avg_hold_time_bars | 19.6095 |
| exposure | 0.3363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
