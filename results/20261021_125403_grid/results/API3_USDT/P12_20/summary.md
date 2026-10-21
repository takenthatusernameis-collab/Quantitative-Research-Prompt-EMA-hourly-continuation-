# EMA Hourly Continuation — API3/USDT P12_20

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -3.0449 |
| sortino_ratio | -0.8407 |
| max_drawdown | 0.6281 |
| cagr | -0.3189 |
| net_avg_win | 61.0880 |
| net_avg_loss | -85.6805 |
| avg_hold_time_bars | 6.7688 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
