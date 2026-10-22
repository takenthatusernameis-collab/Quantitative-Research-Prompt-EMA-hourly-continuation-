# EMA Hourly Continuation — RAY/USDT P12_34

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1255 |
| net_profit_factor | 0.6195 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 1.0450 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -7.1310 |
| sortino_ratio | -3.5712 |
| max_drawdown | 0.9871 |
| cagr | -0.8203 |
| net_avg_win | 27.5967 |
| net_avg_loss | -38.5246 |
| avg_hold_time_bars | 4.1347 |
| exposure | 0.2359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
