# EMA Hourly Continuation — CRO/USDT P21_50

**Symbol:** CRO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.8682 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -3.6315 |
| sortino_ratio | -1.1302 |
| max_drawdown | 0.7360 |
| cagr | -0.4045 |
| net_avg_win | 45.2561 |
| net_avg_loss | -69.0269 |
| avg_hold_time_bars | 7.9514 |
| exposure | 0.1710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
