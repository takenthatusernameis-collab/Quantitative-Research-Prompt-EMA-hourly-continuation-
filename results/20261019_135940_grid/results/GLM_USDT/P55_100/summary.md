# EMA Hourly Continuation — GLM/USDT P55_100

**Symbol:** GLM/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.4622 |
| net_win_rate | 0.4493 |
| gross_profit_factor | 0.8465 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -5.5707 |
| sortino_ratio | -1.9534 |
| max_drawdown | 0.9054 |
| cagr | -0.6077 |
| net_avg_win | 28.2767 |
| net_avg_loss | -49.9186 |
| avg_hold_time_bars | 5.8088 |
| exposure | 0.1616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
