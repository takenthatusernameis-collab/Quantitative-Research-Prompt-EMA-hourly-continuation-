# EMA Hourly Continuation — VR/USDT P55_100

**Symbol:** VR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.5798 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.7715 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -2.7732 |
| sortino_ratio | -0.6034 |
| max_drawdown | 0.5038 |
| cagr | -0.2435 |
| net_avg_win | 68.8249 |
| net_avg_loss | -88.8087 |
| avg_hold_time_bars | 9.8136 |
| exposure | 0.1053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
