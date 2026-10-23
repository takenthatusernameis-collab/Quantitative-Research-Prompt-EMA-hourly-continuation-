# EMA Hourly Continuation — GLM/USDT P12_200

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 459 |
| net_profit_factor | 0.6500 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.8679 |
| sortino_ratio | -0.8662 |
| max_drawdown | 0.6554 |
| cagr | -0.3374 |
| net_avg_win | 54.8851 |
| net_avg_loss | -76.3800 |
| avg_hold_time_bars | 33.3900 |
| exposure | 0.6966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
