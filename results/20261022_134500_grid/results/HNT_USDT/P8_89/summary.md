# EMA Hourly Continuation — HNT/USDT P8_89

**Symbol:** HNT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 830 |
| net_profit_factor | 0.5379 |
| net_win_rate | 0.4446 |
| gross_profit_factor | 0.7768 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -5.2076 |
| sortino_ratio | -2.0969 |
| max_drawdown | 0.9262 |
| cagr | -0.6375 |
| net_avg_win | 29.0820 |
| net_avg_loss | -43.2732 |
| avg_hold_time_bars | 15.9482 |
| exposure | 0.6017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
