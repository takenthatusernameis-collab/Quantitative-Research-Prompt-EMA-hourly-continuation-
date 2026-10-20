# EMA Hourly Continuation — KSM/USDT P21_144

**Symbol:** KSM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.5734 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.8679 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.8182 |
| sortino_ratio | -1.0497 |
| max_drawdown | 0.7337 |
| cagr | -0.4072 |
| net_avg_win | 56.4629 |
| net_avg_loss | -77.1856 |
| avg_hold_time_bars | 33.7045 |
| exposure | 0.6067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
