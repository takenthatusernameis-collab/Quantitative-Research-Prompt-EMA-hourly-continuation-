# EMA Hourly Continuation — GMEE/USDT P26_34

**Symbol:** GMEE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1098 |
| net_profit_factor | 0.2595 |
| net_win_rate | 0.3798 |
| gross_profit_factor | 0.5566 |
| gross_win_rate | 0.3980 |
| sharpe_ratio | -12.2652 |
| sortino_ratio | -5.8055 |
| max_drawdown | 0.9995 |
| cagr | -0.9516 |
| net_avg_win | 8.4017 |
| net_avg_loss | -19.8216 |
| avg_hold_time_bars | 2.3634 |
| exposure | 0.1180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
