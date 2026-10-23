# EMA Hourly Continuation — WIN/USDT P8_34

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1312 |
| net_profit_factor | 0.3613 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8496 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -10.7614 |
| sortino_ratio | -5.5297 |
| max_drawdown | 0.9991 |
| cagr | -0.9373 |
| net_avg_win | 10.1110 |
| net_avg_loss | -20.7736 |
| avg_hold_time_bars | 6.1189 |
| exposure | 0.3649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
