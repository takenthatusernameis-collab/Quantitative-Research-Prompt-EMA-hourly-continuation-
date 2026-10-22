# EMA Hourly Continuation — SAND/USDT P12_89

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.5177 |
| net_win_rate | 0.4345 |
| gross_profit_factor | 0.8466 |
| gross_win_rate | 0.4462 |
| sharpe_ratio | -5.7062 |
| sortino_ratio | -2.0788 |
| max_drawdown | 0.9247 |
| cagr | -0.6393 |
| net_avg_win | 33.5714 |
| net_avg_loss | -49.8209 |
| avg_hold_time_bars | 17.5538 |
| exposure | 0.5418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
