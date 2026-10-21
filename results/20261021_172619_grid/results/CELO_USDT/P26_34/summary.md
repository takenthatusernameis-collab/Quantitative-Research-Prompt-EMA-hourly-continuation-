# EMA Hourly Continuation — CELO/USDT P26_34

**Symbol:** CELO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 0.9672 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.3051 |
| sortino_ratio | -0.5485 |
| max_drawdown | 0.4735 |
| cagr | -0.2229 |
| net_avg_win | 59.7632 |
| net_avg_loss | -91.6729 |
| avg_hold_time_bars | 4.7899 |
| exposure | 0.0598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
