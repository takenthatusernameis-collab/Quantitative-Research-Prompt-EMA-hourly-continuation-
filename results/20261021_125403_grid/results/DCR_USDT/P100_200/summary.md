# EMA Hourly Continuation — DCR/USDT P100_200

**Symbol:** DCR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.5680 |
| net_win_rate | 0.4361 |
| gross_profit_factor | 0.7911 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -3.0946 |
| sortino_ratio | -0.7653 |
| max_drawdown | 0.5949 |
| cagr | -0.2964 |
| net_avg_win | 58.1383 |
| net_avg_loss | -79.1475 |
| avg_hold_time_bars | 10.6295 |
| exposure | 0.1467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
