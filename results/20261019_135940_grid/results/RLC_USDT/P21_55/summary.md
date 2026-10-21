# EMA Hourly Continuation — RLC/USDT P21_55

**Symbol:** RLC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.4969 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8822 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -6.3228 |
| sortino_ratio | -2.7080 |
| max_drawdown | 0.9650 |
| cagr | -0.7328 |
| net_avg_win | 21.9275 |
| net_avg_loss | -38.9289 |
| avg_hold_time_bars | 5.3402 |
| exposure | 0.2248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
