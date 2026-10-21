# EMA Hourly Continuation — FIL/USDT P8_200

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.8590 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -0.6901 |
| sortino_ratio | -0.1490 |
| max_drawdown | 0.2527 |
| cagr | -0.0680 |
| net_avg_win | 85.9072 |
| net_avg_loss | -101.7751 |
| avg_hold_time_bars | 80.5570 |
| exposure | 0.8349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
