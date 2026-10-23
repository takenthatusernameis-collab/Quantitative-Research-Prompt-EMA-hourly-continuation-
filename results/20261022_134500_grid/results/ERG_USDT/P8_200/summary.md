# EMA Hourly Continuation — ERG/USDT P8_200

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.5497 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 0.7979 |
| gross_win_rate | 0.4585 |
| sharpe_ratio | -3.5263 |
| sortino_ratio | -1.0607 |
| max_drawdown | 0.7341 |
| cagr | -0.3975 |
| net_avg_win | 42.2375 |
| net_avg_loss | -63.9345 |
| avg_hold_time_bars | 36.2118 |
| exposure | 0.7539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
