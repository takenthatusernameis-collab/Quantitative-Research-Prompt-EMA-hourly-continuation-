# EMA Hourly Continuation — CSPR/USDT P55_100

**Symbol:** CSPR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.7057 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9205 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -2.1034 |
| sortino_ratio | -0.5512 |
| max_drawdown | 0.4751 |
| cagr | -0.2238 |
| net_avg_win | 70.5393 |
| net_avg_loss | -90.3601 |
| avg_hold_time_bars | 7.1424 |
| exposure | 0.1094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
