# EMA Hourly Continuation — REZ/USDT P50_144

**Symbol:** REZ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.8003 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -1.5161 |
| sortino_ratio | -0.4591 |
| max_drawdown | 0.4690 |
| cagr | -0.1980 |
| net_avg_win | 72.3642 |
| net_avg_loss | -96.6419 |
| avg_hold_time_bars | 15.5188 |
| exposure | 0.3229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
