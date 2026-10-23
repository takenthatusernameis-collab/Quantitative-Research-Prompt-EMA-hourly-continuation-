# EMA Hourly Continuation — CELO/USDT P26_100

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.6805 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 1.0485 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -3.0968 |
| sortino_ratio | -1.0539 |
| max_drawdown | 0.7279 |
| cagr | -0.3937 |
| net_avg_win | 53.5760 |
| net_avg_loss | -75.2989 |
| avg_hold_time_bars | 14.7496 |
| exposure | 0.3891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
