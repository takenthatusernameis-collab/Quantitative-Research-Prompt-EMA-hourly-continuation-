# EMA Hourly Continuation — TRAC/USDT P89_200

**Symbol:** TRAC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8149 |
| net_win_rate | 0.5102 |
| gross_profit_factor | 1.0306 |
| gross_win_rate | 0.5102 |
| sharpe_ratio | -1.0411 |
| sortino_ratio | -0.2562 |
| max_drawdown | 0.2795 |
| cagr | -0.1120 |
| net_avg_win | 75.7182 |
| net_avg_loss | -96.7854 |
| avg_hold_time_bars | 14.2211 |
| exposure | 0.1900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
