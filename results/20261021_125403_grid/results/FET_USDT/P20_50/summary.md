# EMA Hourly Continuation — FET/USDT P20_50

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.7073 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -2.4830 |
| sortino_ratio | -0.7506 |
| max_drawdown | 0.6171 |
| cagr | -0.2914 |
| net_avg_win | 66.9266 |
| net_avg_loss | -81.7219 |
| avg_hold_time_bars | 7.9224 |
| exposure | 0.1624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
