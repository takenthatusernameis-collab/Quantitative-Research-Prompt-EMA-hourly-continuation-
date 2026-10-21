# EMA Hourly Continuation — SEI/USDT P8_200

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.9958 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1490 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | 0.0265 |
| sortino_ratio | 0.0057 |
| max_drawdown | 0.1247 |
| cagr | -0.0019 |
| net_avg_win | 95.1619 |
| net_avg_loss | -111.4901 |
| avg_hold_time_bars | 83.1176 |
| exposure | 0.8350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
