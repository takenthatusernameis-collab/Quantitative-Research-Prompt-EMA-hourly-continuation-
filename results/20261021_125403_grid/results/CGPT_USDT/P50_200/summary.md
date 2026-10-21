# EMA Hourly Continuation — CGPT/USDT P50_200

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8061 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9560 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -1.2054 |
| sortino_ratio | -0.2949 |
| max_drawdown | 0.2979 |
| cagr | -0.1281 |
| net_avg_win | 84.6425 |
| net_avg_loss | -99.4451 |
| avg_hold_time_bars | 28.4048 |
| exposure | 0.3796 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
