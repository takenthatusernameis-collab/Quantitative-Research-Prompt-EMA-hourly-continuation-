# EMA Hourly Continuation — DASH/USDT P21_26

**Symbol:** DASH/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1223 |
| net_profit_factor | 0.1337 |
| net_win_rate | 0.3385 |
| gross_profit_factor | 0.6450 |
| gross_win_rate | 0.3974 |
| sharpe_ratio | -15.7848 |
| sortino_ratio | -8.1182 |
| max_drawdown | 1.0000 |
| cagr | -0.9885 |
| net_avg_win | 3.7279 |
| net_avg_loss | -14.2685 |
| avg_hold_time_bars | 1.8397 |
| exposure | 0.1023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
