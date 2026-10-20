# EMA Hourly Continuation — GLM/USDT P12_26

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1316 |
| net_profit_factor | 0.4013 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.8724 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -9.9256 |
| sortino_ratio | -5.1060 |
| max_drawdown | 0.9982 |
| cagr | -0.9199 |
| net_avg_win | 11.4567 |
| net_avg_loss | -22.7774 |
| avg_hold_time_bars | 3.6938 |
| exposure | 0.2210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
