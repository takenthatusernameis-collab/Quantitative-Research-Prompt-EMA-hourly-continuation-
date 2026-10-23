# EMA Hourly Continuation — ARPA/USDT P50_200

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 481 |
| net_profit_factor | 0.5400 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.8120 |
| gross_win_rate | 0.4449 |
| sharpe_ratio | -4.3839 |
| sortino_ratio | -1.3479 |
| max_drawdown | 0.8156 |
| cagr | -0.4759 |
| net_avg_win | 45.1555 |
| net_avg_loss | -64.2552 |
| avg_hold_time_bars | 17.1954 |
| exposure | 0.3743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
