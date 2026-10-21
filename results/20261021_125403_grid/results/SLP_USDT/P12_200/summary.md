# EMA Hourly Continuation — SLP/USDT P12_200

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7739 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -1.5226 |
| sortino_ratio | -0.4051 |
| max_drawdown | 0.4044 |
| cagr | -0.1712 |
| net_avg_win | 76.5944 |
| net_avg_loss | -91.8679 |
| avg_hold_time_bars | 45.2092 |
| exposure | 0.7172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
