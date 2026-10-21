# EMA Hourly Continuation — POL/USDT P89_100

**Symbol:** POL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 109 |
| net_profit_factor | 0.5115 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.7531 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -2.0122 |
| sortino_ratio | -0.3006 |
| max_drawdown | 0.3078 |
| cagr | -0.1294 |
| net_avg_win | 64.1058 |
| net_avg_loss | -98.6177 |
| avg_hold_time_bars | 5.1009 |
| exposure | 0.0253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
