# EMA Hourly Continuation — AERO/USDT P89_200

**Symbol:** AERO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.5865 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -3.1051 |
| sortino_ratio | -0.7998 |
| max_drawdown | 0.6234 |
| cagr | -0.3222 |
| net_avg_win | 57.0432 |
| net_avg_loss | -81.9343 |
| avg_hold_time_bars | 11.1386 |
| exposure | 0.1716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
