# EMA Hourly Continuation — ANYONE/USDT P55_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.6499 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.7842 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -2.2825 |
| sortino_ratio | -0.5976 |
| max_drawdown | 0.4865 |
| cagr | -0.2404 |
| net_avg_win | 62.2260 |
| net_avg_loss | -78.1861 |
| avg_hold_time_bars | 7.5081 |
| exposure | 0.1165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
