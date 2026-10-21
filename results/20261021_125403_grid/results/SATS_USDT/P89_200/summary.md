# EMA Hourly Continuation — SATS/USDT P89_200

**Symbol:** SATS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.6165 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.7801 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -2.4297 |
| sortino_ratio | -0.5664 |
| max_drawdown | 0.4976 |
| cagr | -0.2290 |
| net_avg_win | 64.4638 |
| net_avg_loss | -82.5447 |
| avg_hold_time_bars | 16.5625 |
| exposure | 0.2039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
