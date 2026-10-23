# EMA Hourly Continuation — GMX/USDT P20_144

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.6016 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8635 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -4.1211 |
| sortino_ratio | -1.4201 |
| max_drawdown | 0.8236 |
| cagr | -0.4885 |
| net_avg_win | 45.8883 |
| net_avg_loss | -61.3855 |
| avg_hold_time_bars | 18.3894 |
| exposure | 0.5024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
