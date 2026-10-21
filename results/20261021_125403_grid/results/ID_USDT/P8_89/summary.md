# EMA Hourly Continuation — ID/USDT P8_89

**Symbol:** ID/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.7936 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -1.7750 |
| sortino_ratio | -0.5772 |
| max_drawdown | 0.5263 |
| cagr | -0.2351 |
| net_avg_win | 73.5334 |
| net_avg_loss | -89.8553 |
| avg_hold_time_bars | 27.5939 |
| exposure | 0.6519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
