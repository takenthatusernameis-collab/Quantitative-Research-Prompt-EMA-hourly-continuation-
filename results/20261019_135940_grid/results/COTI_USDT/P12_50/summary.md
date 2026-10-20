# EMA Hourly Continuation — COTI/USDT P12_50

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.5716 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8881 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -6.7958 |
| sortino_ratio | -3.2695 |
| max_drawdown | 0.9813 |
| cagr | -0.7909 |
| net_avg_win | 25.1510 |
| net_avg_loss | -35.5865 |
| avg_hold_time_bars | 6.1917 |
| exposure | 0.3273 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
