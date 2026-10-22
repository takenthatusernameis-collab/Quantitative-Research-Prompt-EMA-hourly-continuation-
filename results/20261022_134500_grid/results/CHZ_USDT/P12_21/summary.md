# EMA Hourly Continuation — CHZ/USDT P12_21

**Symbol:** CHZ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1527 |
| net_profit_factor | 0.3440 |
| net_win_rate | 0.4028 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -13.8704 |
| sortino_ratio | -7.7249 |
| max_drawdown | 1.0000 |
| cagr | -0.9821 |
| net_avg_win | 8.5263 |
| net_avg_loss | -16.7141 |
| avg_hold_time_bars | 2.3687 |
| exposure | 0.1644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
