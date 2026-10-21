# EMA Hourly Continuation — TAO/USDT P55_200

**Symbol:** TAO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.8052 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9485 |
| gross_win_rate | 0.4891 |
| sharpe_ratio | -1.0511 |
| sortino_ratio | -0.2483 |
| max_drawdown | 0.2580 |
| cagr | -0.1089 |
| net_avg_win | 77.5681 |
| net_avg_loss | -92.2013 |
| avg_hold_time_bars | 24.6533 |
| exposure | 0.3070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
