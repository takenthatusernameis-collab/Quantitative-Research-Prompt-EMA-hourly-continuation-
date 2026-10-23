# EMA Hourly Continuation — REZ/USDT P34_144

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.7907 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0511 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -1.7313 |
| sortino_ratio | -0.5438 |
| max_drawdown | 0.5261 |
| cagr | -0.2277 |
| net_avg_win | 72.8493 |
| net_avg_loss | -94.8406 |
| avg_hold_time_bars | 19.1718 |
| exposure | 0.4272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
