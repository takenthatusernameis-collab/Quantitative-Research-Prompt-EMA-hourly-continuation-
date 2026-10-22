# EMA Hourly Continuation — RUNE/USDT P89_144

**Symbol:** RUNE/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.5010 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -4.0991 |
| sortino_ratio | -1.2281 |
| max_drawdown | 0.7791 |
| cagr | -0.4421 |
| net_avg_win | 36.9477 |
| net_avg_loss | -65.0308 |
| avg_hold_time_bars | 5.0448 |
| exposure | 0.1023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
