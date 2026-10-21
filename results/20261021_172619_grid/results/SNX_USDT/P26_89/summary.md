# EMA Hourly Continuation — SNX/USDT P26_89

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.8522 |
| net_win_rate | 0.5214 |
| gross_profit_factor | 1.0774 |
| gross_win_rate | 0.5214 |
| sharpe_ratio | -1.0400 |
| sortino_ratio | -0.3312 |
| max_drawdown | 0.3528 |
| cagr | -0.1437 |
| net_avg_win | 72.9470 |
| net_avg_loss | -93.2437 |
| avg_hold_time_bars | 12.3951 |
| exposure | 0.2754 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
