# EMA Hourly Continuation — PUFFER/USDT P20_21

**Symbol:** PUFFER/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 164 |
| net_profit_factor | 0.7600 |
| net_win_rate | 0.5183 |
| gross_profit_factor | 1.1115 |
| gross_win_rate | 0.5244 |
| sharpe_ratio | -1.2475 |
| sortino_ratio | -0.2564 |
| max_drawdown | 0.2812 |
| cagr | -0.1113 |
| net_avg_win | 78.9378 |
| net_avg_loss | -111.7486 |
| avg_hold_time_bars | 6.7866 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
