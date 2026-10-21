# EMA Hourly Continuation — TRAC/USDT P21_89

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.8949 |
| net_win_rate | 0.5274 |
| gross_profit_factor | 1.1165 |
| gross_win_rate | 0.5274 |
| sharpe_ratio | -0.7632 |
| sortino_ratio | -0.2444 |
| max_drawdown | 0.3568 |
| cagr | -0.1101 |
| net_avg_win | 83.1771 |
| net_avg_loss | -103.7128 |
| avg_hold_time_bars | 14.2941 |
| exposure | 0.3203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
