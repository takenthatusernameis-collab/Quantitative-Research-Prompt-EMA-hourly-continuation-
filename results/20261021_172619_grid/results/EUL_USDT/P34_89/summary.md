# EMA Hourly Continuation — EUL/USDT P34_89

**Symbol:** EUL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.6229 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.7992 |
| gross_win_rate | 0.4539 |
| sharpe_ratio | -2.7343 |
| sortino_ratio | -0.7884 |
| max_drawdown | 0.6146 |
| cagr | -0.3045 |
| net_avg_win | 52.8598 |
| net_avg_loss | -70.5237 |
| avg_hold_time_bars | 11.7306 |
| exposure | 0.2197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
