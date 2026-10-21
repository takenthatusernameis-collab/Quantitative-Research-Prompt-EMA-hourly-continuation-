# EMA Hourly Continuation — CHR/USDT P55_89

**Symbol:** CHR/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6140 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8148 |
| gross_win_rate | 0.4557 |
| sharpe_ratio | -2.8474 |
| sortino_ratio | -0.7932 |
| max_drawdown | 0.6383 |
| cagr | -0.3050 |
| net_avg_win | 54.5980 |
| net_avg_loss | -74.4504 |
| avg_hold_time_bars | 6.2161 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
