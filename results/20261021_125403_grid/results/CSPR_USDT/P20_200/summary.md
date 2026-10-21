# EMA Hourly Continuation — CSPR/USDT P20_200

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.6984 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8474 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -2.0968 |
| sortino_ratio | -0.5843 |
| max_drawdown | 0.5369 |
| cagr | -0.2360 |
| net_avg_win | 63.5584 |
| net_avg_loss | -78.7014 |
| avg_hold_time_bars | 33.4430 |
| exposure | 0.5868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
