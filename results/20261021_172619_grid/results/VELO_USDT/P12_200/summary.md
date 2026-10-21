# EMA Hourly Continuation — VELO/USDT P12_200

**Symbol:** VELO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.9932 |
| net_win_rate | 0.5310 |
| gross_profit_factor | 1.1182 |
| gross_win_rate | 0.5310 |
| sharpe_ratio | 0.0205 |
| sortino_ratio | 0.0054 |
| max_drawdown | 0.2083 |
| cagr | -0.0044 |
| net_avg_win | 87.9752 |
| net_avg_loss | -100.2802 |
| avg_hold_time_bars | 44.9853 |
| exposure | 0.6932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
