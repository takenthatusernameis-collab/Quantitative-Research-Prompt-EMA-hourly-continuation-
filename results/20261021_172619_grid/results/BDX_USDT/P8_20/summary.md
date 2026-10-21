# EMA Hourly Continuation — BDX/USDT P8_20

**Symbol:** BDX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.3056 |
| net_win_rate | 0.3102 |
| gross_profit_factor | 0.5119 |
| gross_win_rate | 0.3135 |
| sharpe_ratio | -6.5615 |
| sortino_ratio | -1.6467 |
| max_drawdown | 0.8588 |
| cagr | -0.5414 |
| net_avg_win | 40.2110 |
| net_avg_loss | -59.1763 |
| avg_hold_time_bars | 4.5314 |
| exposure | 0.0624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
