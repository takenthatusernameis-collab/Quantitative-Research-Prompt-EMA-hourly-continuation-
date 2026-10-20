# EMA Hourly Continuation — COTI/USDT P21_26

**Symbol:** COTI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1226 |
| net_profit_factor | 0.3153 |
| net_win_rate | 0.3744 |
| gross_profit_factor | 0.8015 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -13.4410 |
| sortino_ratio | -6.8093 |
| max_drawdown | 0.9999 |
| cagr | -0.9715 |
| net_avg_win | 10.0291 |
| net_avg_loss | -19.0378 |
| avg_hold_time_bars | 1.7594 |
| exposure | 0.0980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
