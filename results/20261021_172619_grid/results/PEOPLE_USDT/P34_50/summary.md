# EMA Hourly Continuation — PEOPLE/USDT P34_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7361 |
| net_win_rate | 0.5076 |
| gross_profit_factor | 1.0257 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -1.7378 |
| sortino_ratio | -0.4510 |
| max_drawdown | 0.4121 |
| cagr | -0.1858 |
| net_avg_win | 67.9724 |
| net_avg_loss | -95.2102 |
| avg_hold_time_bars | 5.0642 |
| exposure | 0.0749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
