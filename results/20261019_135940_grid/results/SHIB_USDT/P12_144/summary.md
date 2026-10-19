# EMA Hourly Continuation — SHIB/USDT P12_144

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6840 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0863 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -2.9096 |
| sortino_ratio | -0.9312 |
| max_drawdown | 0.6925 |
| cagr | -0.3630 |
| net_avg_win | 55.9811 |
| net_avg_loss | -82.7972 |
| avg_hold_time_bars | 27.1305 |
| exposure | 0.6425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
