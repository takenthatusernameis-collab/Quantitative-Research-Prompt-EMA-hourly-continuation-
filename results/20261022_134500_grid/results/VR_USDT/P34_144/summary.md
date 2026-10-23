# EMA Hourly Continuation — VR/USDT P34_144

**Symbol:** VR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.4609 |
| net_win_rate | 0.3258 |
| gross_profit_factor | 0.6818 |
| gross_win_rate | 0.3403 |
| sharpe_ratio | -9.6302 |
| sortino_ratio | -3.3357 |
| max_drawdown | 0.9919 |
| cagr | -0.8528 |
| net_avg_win | 41.9815 |
| net_avg_loss | -44.0167 |
| avg_hold_time_bars | 13.8839 |
| exposure | 0.3913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
