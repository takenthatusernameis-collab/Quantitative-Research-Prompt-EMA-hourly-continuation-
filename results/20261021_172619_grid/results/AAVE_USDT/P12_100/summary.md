# EMA Hourly Continuation — AAVE/USDT P12_100

**Symbol:** AAVE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9217 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -1.8043 |
| sortino_ratio | -0.5247 |
| max_drawdown | 0.5022 |
| cagr | -0.2151 |
| net_avg_win | 74.1362 |
| net_avg_loss | -88.5789 |
| avg_hold_time_bars | 29.6715 |
| exposure | 0.5624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
