# EMA Hourly Continuation — MTL/USDT P100_144

**Symbol:** MTL/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6246 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4893 |
| sharpe_ratio | -2.4183 |
| sortino_ratio | -0.5793 |
| max_drawdown | 0.4919 |
| cagr | -0.2333 |
| net_avg_win | 59.7296 |
| net_avg_loss | -90.3192 |
| avg_hold_time_bars | 9.5143 |
| exposure | 0.1206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
