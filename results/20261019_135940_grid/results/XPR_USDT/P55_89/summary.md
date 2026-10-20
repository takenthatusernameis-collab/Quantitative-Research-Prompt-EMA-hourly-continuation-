# EMA Hourly Continuation — XPR/USDT P55_89

**Symbol:** XPR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.2814 |
| net_win_rate | 0.3606 |
| gross_profit_factor | 0.6429 |
| gross_win_rate | 0.3795 |
| sharpe_ratio | -9.7526 |
| sortino_ratio | -3.5471 |
| max_drawdown | 0.9905 |
| cagr | -0.8427 |
| net_avg_win | 16.9368 |
| net_avg_loss | -33.9466 |
| avg_hold_time_bars | 3.8315 |
| exposure | 0.1106 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
