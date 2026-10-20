# EMA Hourly Continuation — SUPER/USDT P20_50

**Symbol:** SUPER/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 975 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -5.8590 |
| sortino_ratio | -2.5848 |
| max_drawdown | 0.9575 |
| cagr | -0.7115 |
| net_avg_win | 22.2559 |
| net_avg_loss | -38.5586 |
| avg_hold_time_bars | 5.0092 |
| exposure | 0.2220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
