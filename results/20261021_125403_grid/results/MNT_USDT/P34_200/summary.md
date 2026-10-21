# EMA Hourly Continuation — MNT/USDT P34_200

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8435 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0411 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -0.7173 |
| sortino_ratio | -0.1554 |
| max_drawdown | 0.2339 |
| cagr | -0.0706 |
| net_avg_win | 77.3634 |
| net_avg_loss | -96.6775 |
| avg_hold_time_bars | 54.6623 |
| exposure | 0.5665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
