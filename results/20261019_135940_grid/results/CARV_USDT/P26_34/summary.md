# EMA Hourly Continuation — CARV/USDT P26_34

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.2962 |
| net_win_rate | 0.4135 |
| gross_profit_factor | 0.7561 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -9.6105 |
| sortino_ratio | -4.1345 |
| max_drawdown | 0.9862 |
| cagr | -0.8789 |
| net_avg_win | 13.5623 |
| net_avg_loss | -32.2855 |
| avg_hold_time_bars | 3.3378 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
