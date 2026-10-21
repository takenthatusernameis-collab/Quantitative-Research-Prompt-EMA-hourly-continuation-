# EMA Hourly Continuation — CFX/USDT P26_89

**Symbol:** CFX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.7690 |
| net_win_rate | 0.4953 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4953 |
| sharpe_ratio | -1.7664 |
| sortino_ratio | -0.5240 |
| max_drawdown | 0.4807 |
| cagr | -0.2142 |
| net_avg_win | 70.9701 |
| net_avg_loss | -90.5931 |
| avg_hold_time_bars | 16.3651 |
| exposure | 0.3199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
