# EMA Hourly Continuation — CTC/USDT P100_144

**Symbol:** CTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.7673 |
| net_win_rate | 0.5297 |
| gross_profit_factor | 1.1352 |
| gross_win_rate | 0.5297 |
| sharpe_ratio | -1.3052 |
| sortino_ratio | -0.2898 |
| max_drawdown | 0.3073 |
| cagr | -0.1240 |
| net_avg_win | 74.6230 |
| net_avg_loss | -109.5143 |
| avg_hold_time_bars | 6.2542 |
| exposure | 0.0671 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
