# EMA Hourly Continuation — ARKM/USDT P12_144

**Symbol:** ARKM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.8317 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9588 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -0.9599 |
| sortino_ratio | -0.2485 |
| max_drawdown | 0.2927 |
| cagr | -0.1098 |
| net_avg_win | 76.8102 |
| net_avg_loss | -90.6792 |
| avg_hold_time_bars | 46.9210 |
| exposure | 0.7017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
