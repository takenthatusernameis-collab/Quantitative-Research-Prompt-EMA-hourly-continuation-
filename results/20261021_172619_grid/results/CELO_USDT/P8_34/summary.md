# EMA Hourly Continuation — CELO/USDT P8_34

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 799 |
| net_profit_factor | 0.7111 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9477 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -3.1910 |
| sortino_ratio | -1.2861 |
| max_drawdown | 0.7743 |
| cagr | -0.4457 |
| net_avg_win | 49.2532 |
| net_avg_loss | -65.0579 |
| avg_hold_time_bars | 8.6245 |
| exposure | 0.3118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
