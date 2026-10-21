# EMA Hourly Continuation — ALGO/USDT P21_34

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.7846 |
| net_win_rate | 0.5315 |
| gross_profit_factor | 1.1173 |
| gross_win_rate | 0.5315 |
| sharpe_ratio | -1.1382 |
| sortino_ratio | -0.2623 |
| max_drawdown | 0.2958 |
| cagr | -0.1135 |
| net_avg_win | 70.4047 |
| net_avg_loss | -101.8016 |
| avg_hold_time_bars | 4.8622 |
| exposure | 0.0561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
