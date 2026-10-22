# EMA Hourly Continuation — BDX/USDT P89_200

**Symbol:** BDX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 857 |
| net_profit_factor | 0.2571 |
| net_win_rate | 0.3092 |
| gross_profit_factor | 0.6026 |
| gross_win_rate | 0.3536 |
| sharpe_ratio | -13.7269 |
| sortino_ratio | -5.9083 |
| max_drawdown | 0.9997 |
| cagr | -0.9620 |
| net_avg_win | 13.0550 |
| net_avg_loss | -22.7312 |
| avg_hold_time_bars | 5.4702 |
| exposure | 0.2131 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
