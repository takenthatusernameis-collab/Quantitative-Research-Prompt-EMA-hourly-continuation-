# EMA Hourly Continuation — ID/USDT P8_55

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.6339 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 1.0156 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -4.6303 |
| sortino_ratio | -1.9489 |
| max_drawdown | 0.9089 |
| cagr | -0.6071 |
| net_avg_win | 36.1930 |
| net_avg_loss | -52.6044 |
| avg_hold_time_bars | 12.6257 |
| exposure | 0.5160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
