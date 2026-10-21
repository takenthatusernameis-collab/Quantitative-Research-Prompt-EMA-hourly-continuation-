# EMA Hourly Continuation — DEXE/USDT P21_89

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.8160 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0151 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -1.1292 |
| sortino_ratio | -0.3316 |
| max_drawdown | 0.4085 |
| cagr | -0.1431 |
| net_avg_win | 66.6225 |
| net_avg_loss | -85.2318 |
| avg_hold_time_bars | 26.6706 |
| exposure | 0.5080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
