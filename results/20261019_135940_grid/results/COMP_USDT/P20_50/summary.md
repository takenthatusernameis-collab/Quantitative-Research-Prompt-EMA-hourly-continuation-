# EMA Hourly Continuation — COMP/USDT P20_50

**Symbol:** COMP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1092 |
| net_profit_factor | 0.4179 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8401 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -7.5195 |
| sortino_ratio | -3.5122 |
| max_drawdown | 0.9866 |
| cagr | -0.8204 |
| net_avg_win | 13.9176 |
| net_avg_loss | -29.0737 |
| avg_hold_time_bars | 4.9093 |
| exposure | 0.2437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
