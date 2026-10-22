# EMA Hourly Continuation — ALGO/USDT P89_200

**Symbol:** ALGO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.5608 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8871 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.6016 |
| sortino_ratio | -0.9853 |
| max_drawdown | 0.6932 |
| cagr | -0.3731 |
| net_avg_win | 51.8468 |
| net_avg_loss | -77.0492 |
| avg_hold_time_bars | 10.5775 |
| exposure | 0.1798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
