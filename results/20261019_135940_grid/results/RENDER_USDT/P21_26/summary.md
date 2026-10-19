# EMA Hourly Continuation — RENDER/USDT P21_26

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.2146 |
| net_win_rate | 0.3407 |
| gross_profit_factor | 0.5726 |
| gross_win_rate | 0.3866 |
| sharpe_ratio | -14.7253 |
| sortino_ratio | -7.2894 |
| max_drawdown | 0.9998 |
| cagr | -0.9809 |
| net_avg_win | 8.0115 |
| net_avg_loss | -19.2879 |
| avg_hold_time_bars | 1.9970 |
| exposure | 0.1055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
