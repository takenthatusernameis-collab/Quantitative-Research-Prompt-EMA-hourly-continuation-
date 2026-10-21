# EMA Hourly Continuation — WAVES/USDT P8_34

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 738 |
| net_profit_factor | 0.6624 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9361 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -3.7934 |
| sortino_ratio | -1.4733 |
| max_drawdown | 0.8238 |
| cagr | -0.4925 |
| net_avg_win | 45.2122 |
| net_avg_loss | -63.2619 |
| avg_hold_time_bars | 7.9837 |
| exposure | 0.2678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
