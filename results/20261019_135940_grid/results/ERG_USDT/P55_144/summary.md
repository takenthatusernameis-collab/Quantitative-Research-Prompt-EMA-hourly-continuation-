# EMA Hourly Continuation — ERG/USDT P55_144

**Symbol:** ERG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.3810 |
| net_win_rate | 0.3982 |
| gross_profit_factor | 0.6413 |
| gross_win_rate | 0.4055 |
| sharpe_ratio | -6.4042 |
| sortino_ratio | -2.0917 |
| max_drawdown | 0.9280 |
| cagr | -0.6483 |
| net_avg_win | 26.3034 |
| net_avg_loss | -45.6800 |
| avg_hold_time_bars | 10.1284 |
| exposure | 0.2509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
