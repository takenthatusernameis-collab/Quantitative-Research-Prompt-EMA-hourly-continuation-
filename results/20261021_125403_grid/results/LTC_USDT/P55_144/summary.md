# EMA Hourly Continuation — LTC/USDT P55_144

**Symbol:** LTC/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.5703 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8159 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -2.9645 |
| sortino_ratio | -0.7777 |
| max_drawdown | 0.6068 |
| cagr | -0.3001 |
| net_avg_win | 50.6722 |
| net_avg_loss | -75.2598 |
| avg_hold_time_bars | 15.3817 |
| exposure | 0.2363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
