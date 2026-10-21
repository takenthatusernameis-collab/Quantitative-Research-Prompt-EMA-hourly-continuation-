# EMA Hourly Continuation — ANYONE/USDT P20_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.7622 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.8805 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -1.9671 |
| sortino_ratio | -0.6363 |
| max_drawdown | 0.5089 |
| cagr | -0.2553 |
| net_avg_win | 71.1451 |
| net_avg_loss | -82.4319 |
| avg_hold_time_bars | 14.1520 |
| exposure | 0.3340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
