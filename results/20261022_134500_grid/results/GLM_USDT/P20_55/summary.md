# EMA Hourly Continuation — GLM/USDT P20_55

**Symbol:** GLM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 878 |
| net_profit_factor | 0.4388 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.7702 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -6.7161 |
| sortino_ratio | -2.8204 |
| max_drawdown | 0.9668 |
| cagr | -0.7416 |
| net_avg_win | 18.9874 |
| net_avg_loss | -35.8810 |
| avg_hold_time_bars | 6.8417 |
| exposure | 0.2730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
