# EMA Hourly Continuation — GLM/USDT P20_50

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 904 |
| net_profit_factor | 0.4276 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -6.9062 |
| sortino_ratio | -2.9323 |
| max_drawdown | 0.9724 |
| cagr | -0.7589 |
| net_avg_win | 17.6260 |
| net_avg_loss | -34.5144 |
| avg_hold_time_bars | 6.1692 |
| exposure | 0.2535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
