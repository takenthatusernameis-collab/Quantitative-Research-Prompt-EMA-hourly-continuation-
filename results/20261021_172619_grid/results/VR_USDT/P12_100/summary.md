# EMA Hourly Continuation — VR/USDT P12_100

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7208 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -1.9147 |
| sortino_ratio | -0.5403 |
| max_drawdown | 0.4719 |
| cagr | -0.2217 |
| net_avg_win | 64.8543 |
| net_avg_loss | -79.6893 |
| avg_hold_time_bars | 29.0556 |
| exposure | 0.5230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
