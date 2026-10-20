# EMA Hourly Continuation — BIGTIME/USDT P50_144

**Symbol:** BIGTIME/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7142 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 1.0309 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.4805 |
| sortino_ratio | -0.7556 |
| max_drawdown | 0.6215 |
| cagr | -0.3019 |
| net_avg_win | 64.1971 |
| net_avg_loss | -88.3656 |
| avg_hold_time_bars | 13.9038 |
| exposure | 0.2945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
