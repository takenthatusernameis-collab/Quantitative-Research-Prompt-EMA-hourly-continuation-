# EMA Hourly Continuation — METIS/USDT P21_34

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.3591 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.8177 |
| gross_win_rate | 0.4202 |
| sharpe_ratio | -11.2559 |
| sortino_ratio | -5.4460 |
| max_drawdown | 0.9991 |
| cagr | -0.9370 |
| net_avg_win | 12.1409 |
| net_avg_loss | -22.3313 |
| avg_hold_time_bars | 2.6195 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
