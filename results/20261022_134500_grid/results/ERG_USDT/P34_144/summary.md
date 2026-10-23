# EMA Hourly Continuation — ERG/USDT P34_144

**Symbol:** ERG/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.3809 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.5850 |
| gross_win_rate | 0.4007 |
| sharpe_ratio | -6.1252 |
| sortino_ratio | -2.0041 |
| max_drawdown | 0.9199 |
| cagr | -0.6307 |
| net_avg_win | 25.9118 |
| net_avg_loss | -44.8014 |
| avg_hold_time_bars | 15.1275 |
| exposure | 0.3775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
