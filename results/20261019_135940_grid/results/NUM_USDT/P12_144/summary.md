# EMA Hourly Continuation — NUM/USDT P12_144

**Symbol:** NUM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.5975 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.8138 |
| gross_win_rate | 0.4257 |
| sharpe_ratio | -4.4008 |
| sortino_ratio | -1.4424 |
| max_drawdown | 0.8341 |
| cagr | -0.4956 |
| net_avg_win | 53.4375 |
| net_avg_loss | -64.3249 |
| avg_hold_time_bars | 25.6991 |
| exposure | 0.6366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
