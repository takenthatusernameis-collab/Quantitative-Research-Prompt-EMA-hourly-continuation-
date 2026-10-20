# EMA Hourly Continuation — DUSK/USDT P8_34

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1346 |
| net_profit_factor | 0.6690 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 1.0883 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -6.5812 |
| sortino_ratio | -3.3969 |
| max_drawdown | 0.9843 |
| cagr | -0.8039 |
| net_avg_win | 31.7974 |
| net_avg_loss | -41.2013 |
| avg_hold_time_bars | 5.9153 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
