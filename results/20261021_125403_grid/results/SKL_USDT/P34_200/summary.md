# EMA Hourly Continuation — SKL/USDT P34_200

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7947 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.0962 |
| sortino_ratio | -0.2596 |
| max_drawdown | 0.3518 |
| cagr | -0.1136 |
| net_avg_win | 74.9288 |
| net_avg_loss | -90.9179 |
| avg_hold_time_bars | 44.3309 |
| exposure | 0.5541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
