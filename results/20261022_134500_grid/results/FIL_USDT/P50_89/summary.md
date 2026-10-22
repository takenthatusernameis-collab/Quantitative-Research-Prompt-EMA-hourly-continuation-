# EMA Hourly Continuation — FIL/USDT P50_89

**Symbol:** FIL/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.3980 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.7734 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -7.0906 |
| sortino_ratio | -2.5727 |
| max_drawdown | 0.9627 |
| cagr | -0.7246 |
| net_avg_win | 22.7649 |
| net_avg_loss | -41.3445 |
| avg_hold_time_bars | 4.4256 |
| exposure | 0.1338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
