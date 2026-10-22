# EMA Hourly Continuation — ERG/USDT P12_20

**Symbol:** ERG/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.4381 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.6350 |
| gross_win_rate | 0.3863 |
| sharpe_ratio | -4.2907 |
| sortino_ratio | -1.0136 |
| max_drawdown | 0.7033 |
| cagr | -0.3797 |
| net_avg_win | 50.9069 |
| net_avg_loss | -73.1351 |
| avg_hold_time_bars | 4.9711 |
| exposure | 0.0626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
