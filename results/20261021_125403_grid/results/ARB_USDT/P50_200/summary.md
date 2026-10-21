# EMA Hourly Continuation — ARB/USDT P50_200

**Symbol:** ARB/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8235 |
| net_win_rate | 0.4960 |
| gross_profit_factor | 0.9785 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -0.9396 |
| sortino_ratio | -0.2116 |
| max_drawdown | 0.3010 |
| cagr | -0.0940 |
| net_avg_win | 83.2674 |
| net_avg_loss | -99.4958 |
| avg_hold_time_bars | 37.0363 |
| exposure | 0.4175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
