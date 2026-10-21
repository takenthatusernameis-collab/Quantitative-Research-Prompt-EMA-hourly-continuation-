# EMA Hourly Continuation — OSMO/USDT P89_144

**Symbol:** OSMO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.6632 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9347 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.2042 |
| sortino_ratio | -0.5421 |
| max_drawdown | 0.4684 |
| cagr | -0.2198 |
| net_avg_win | 64.3300 |
| net_avg_loss | -90.0243 |
| avg_hold_time_bars | 8.1322 |
| exposure | 0.1090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
