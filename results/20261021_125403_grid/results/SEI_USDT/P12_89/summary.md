# EMA Hourly Continuation — SEI/USDT P12_89

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.8620 |
| net_win_rate | 0.5054 |
| gross_profit_factor | 1.0258 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.0348 |
| sortino_ratio | -0.3186 |
| max_drawdown | 0.3808 |
| cagr | -0.1392 |
| net_avg_win | 84.0576 |
| net_avg_loss | -99.6580 |
| avg_hold_time_bars | 26.1584 |
| exposure | 0.5481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
