# EMA Hourly Continuation — CELO/USDT P8_100

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.6969 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9770 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -3.1229 |
| sortino_ratio | -1.0741 |
| max_drawdown | 0.7304 |
| cagr | -0.4023 |
| net_avg_win | 58.0472 |
| net_avg_loss | -76.6386 |
| avg_hold_time_bars | 25.1464 |
| exposure | 0.6839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
