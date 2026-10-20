# EMA Hourly Continuation — AVA/USDT P89_144

**Symbol:** AVA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.4425 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -4.5516 |
| sortino_ratio | -1.4348 |
| max_drawdown | 0.8273 |
| cagr | -0.4983 |
| net_avg_win | 28.5273 |
| net_avg_loss | -55.7119 |
| avg_hold_time_bars | 5.2004 |
| exposure | 0.1168 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
