# EMA Hourly Continuation — CSPR/USDT P21_50

**Symbol:** CSPR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1282 |
| net_profit_factor | 0.3308 |
| net_win_rate | 0.3877 |
| gross_profit_factor | 0.7111 |
| gross_win_rate | 0.4072 |
| sharpe_ratio | -11.2048 |
| sortino_ratio | -5.6625 |
| max_drawdown | 0.9992 |
| cagr | -0.9426 |
| net_avg_win | 9.9380 |
| net_avg_loss | -19.0211 |
| avg_hold_time_bars | 3.5593 |
| exposure | 0.2074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
