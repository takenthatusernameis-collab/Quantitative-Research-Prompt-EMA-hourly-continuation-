# EMA Hourly Continuation — AR/USDT P34_144

**Symbol:** AR/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7640 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9102 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -1.5530 |
| sortino_ratio | -0.4280 |
| max_drawdown | 0.4129 |
| cagr | -0.1797 |
| net_avg_win | 70.5169 |
| net_avg_loss | -85.6338 |
| avg_hold_time_bars | 23.9251 |
| exposure | 0.4067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
