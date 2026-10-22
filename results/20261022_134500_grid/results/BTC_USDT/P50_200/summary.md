# EMA Hourly Continuation — BTC/USDT P50_200

**Symbol:** BTC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5219 |
| net_win_rate | 0.4769 |
| gross_profit_factor | 1.0578 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -3.8766 |
| sortino_ratio | -1.0105 |
| max_drawdown | 0.7630 |
| cagr | -0.3928 |
| net_avg_win | 44.5619 |
| net_avg_loss | -77.8431 |
| avg_hold_time_bars | 22.4821 |
| exposure | 0.3507 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
