# EMA Hourly Continuation — ZPAY/USDT P8_89

**Symbol:** ZPAY/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.4855 |
| net_win_rate | 0.3398 |
| gross_profit_factor | 0.6146 |
| gross_win_rate | 0.3417 |
| sharpe_ratio | -5.9225 |
| sortino_ratio | -1.8751 |
| max_drawdown | 0.8962 |
| cagr | -0.5838 |
| net_avg_win | 47.7445 |
| net_avg_loss | -50.6063 |
| avg_hold_time_bars | 26.4537 |
| exposure | 0.6201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
