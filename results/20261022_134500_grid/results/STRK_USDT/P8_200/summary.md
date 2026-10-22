# EMA Hourly Continuation — STRK/USDT P8_200

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7264 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9655 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -1.9065 |
| sortino_ratio | -0.5046 |
| max_drawdown | 0.4719 |
| cagr | -0.2143 |
| net_avg_win | 69.7225 |
| net_avg_loss | -91.2395 |
| avg_hold_time_bars | 50.3549 |
| exposure | 0.8125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
