# EMA Hourly Continuation — GLM/USDT P12_144

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.7522 |
| net_win_rate | 0.4977 |
| gross_profit_factor | 0.9841 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.7593 |
| sortino_ratio | -0.5240 |
| max_drawdown | 0.4768 |
| cagr | -0.2147 |
| net_avg_win | 63.9579 |
| net_avg_loss | -84.2428 |
| avg_hold_time_bars | 32.7212 |
| exposure | 0.6455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
