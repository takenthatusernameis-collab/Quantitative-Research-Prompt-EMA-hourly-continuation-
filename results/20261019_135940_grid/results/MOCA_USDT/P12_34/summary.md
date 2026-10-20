# EMA Hourly Continuation — MOCA/USDT P12_34

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1133 |
| net_profit_factor | 0.4773 |
| net_win_rate | 0.4369 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -8.8784 |
| sortino_ratio | -4.4230 |
| max_drawdown | 0.9931 |
| cagr | -0.8857 |
| net_avg_win | 18.3158 |
| net_avg_loss | -29.7722 |
| avg_hold_time_bars | 4.1430 |
| exposure | 0.2353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
