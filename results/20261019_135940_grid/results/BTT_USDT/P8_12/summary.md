# EMA Hourly Continuation — BTT/USDT P8_12

**Symbol:** BTT/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1926 |
| net_profit_factor | 0.1056 |
| net_win_rate | 0.2196 |
| gross_profit_factor | 0.6252 |
| gross_win_rate | 0.3396 |
| sharpe_ratio | -27.3187 |
| sortino_ratio | -19.5674 |
| max_drawdown | 1.0000 |
| cagr | -1.0000 |
| net_avg_win | 2.7909 |
| net_avg_loss | -7.4388 |
| avg_hold_time_bars | 2.0016 |
| exposure | 0.1752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
