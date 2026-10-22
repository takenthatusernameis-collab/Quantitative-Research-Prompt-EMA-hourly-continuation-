# EMA Hourly Continuation — REZ/USDT P89_144

**Symbol:** REZ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -1.2883 |
| sortino_ratio | -0.3194 |
| max_drawdown | 0.3284 |
| cagr | -0.1371 |
| net_avg_win | 73.4993 |
| net_avg_loss | -94.7893 |
| avg_hold_time_bars | 8.7356 |
| exposure | 0.1189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
