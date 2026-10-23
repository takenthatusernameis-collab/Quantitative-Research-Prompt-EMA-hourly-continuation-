# EMA Hourly Continuation — G/USDT P55_144

**Symbol:** G/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5030 |
| net_win_rate | 0.4496 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4644 |
| sharpe_ratio | -4.4481 |
| sortino_ratio | -1.3647 |
| max_drawdown | 0.7770 |
| cagr | -0.4800 |
| net_avg_win | 41.9260 |
| net_avg_loss | -68.1012 |
| avg_hold_time_bars | 12.5602 |
| exposure | 0.2688 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
