# EMA Hourly Continuation — NYM/USDT P50_200

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.2992 |
| net_win_rate | 0.3639 |
| gross_profit_factor | 0.6044 |
| gross_win_rate | 0.3831 |
| sharpe_ratio | -6.8248 |
| sortino_ratio | -1.9661 |
| max_drawdown | 0.9221 |
| cagr | -0.6360 |
| net_avg_win | 26.0416 |
| net_avg_loss | -49.7811 |
| avg_hold_time_bars | 17.3373 |
| exposure | 0.3270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
