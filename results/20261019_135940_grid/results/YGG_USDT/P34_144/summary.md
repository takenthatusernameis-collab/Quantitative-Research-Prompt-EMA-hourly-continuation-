# EMA Hourly Continuation — YGG/USDT P34_144

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6849 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9635 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -2.7262 |
| sortino_ratio | -0.8466 |
| max_drawdown | 0.6458 |
| cagr | -0.3298 |
| net_avg_win | 59.0290 |
| net_avg_loss | -80.0322 |
| avg_hold_time_bars | 18.6626 |
| exposure | 0.4104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
