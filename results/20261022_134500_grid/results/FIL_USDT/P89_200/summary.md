# EMA Hourly Continuation — FIL/USDT P89_200

**Symbol:** FIL/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6206 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0461 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -3.0078 |
| sortino_ratio | -0.8130 |
| max_drawdown | 0.6538 |
| cagr | -0.3311 |
| net_avg_win | 55.0179 |
| net_avg_loss | -88.6546 |
| avg_hold_time_bars | 10.8280 |
| exposure | 0.1860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
