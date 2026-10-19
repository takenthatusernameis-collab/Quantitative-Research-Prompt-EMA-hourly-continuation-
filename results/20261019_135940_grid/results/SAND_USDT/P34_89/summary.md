# EMA Hourly Continuation — SAND/USDT P34_89

**Symbol:** SAND/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.5175 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -5.5303 |
| sortino_ratio | -1.9631 |
| max_drawdown | 0.9197 |
| cagr | -0.6216 |
| net_avg_win | 33.6521 |
| net_avg_loss | -53.7547 |
| avg_hold_time_bars | 7.8445 |
| exposure | 0.2293 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
