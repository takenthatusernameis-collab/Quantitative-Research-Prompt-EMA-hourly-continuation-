# EMA Hourly Continuation — AERO/USDT P21_100

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.7470 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 1.0211 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -2.4567 |
| sortino_ratio | -0.8500 |
| max_drawdown | 0.6504 |
| cagr | -0.3300 |
| net_avg_win | 63.0480 |
| net_avg_loss | -83.8388 |
| avg_hold_time_bars | 13.8826 |
| exposure | 0.3761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
