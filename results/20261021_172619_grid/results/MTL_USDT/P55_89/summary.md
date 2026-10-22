# EMA Hourly Continuation — MTL/USDT P55_89

**Symbol:** MTL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.5397 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4355 |
| sharpe_ratio | -3.9097 |
| sortino_ratio | -1.0738 |
| max_drawdown | 0.7132 |
| cagr | -0.3905 |
| net_avg_win | 51.6105 |
| net_avg_loss | -73.7755 |
| avg_hold_time_bars | 9.0538 |
| exposure | 0.1524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
