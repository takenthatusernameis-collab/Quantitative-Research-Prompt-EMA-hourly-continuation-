# EMA Hourly Continuation — FET/USDT P21_200

**Symbol:** FET/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8370 |
| net_win_rate | 0.5135 |
| gross_profit_factor | 1.0400 |
| gross_win_rate | 0.5135 |
| sharpe_ratio | -0.8565 |
| sortino_ratio | -0.2103 |
| max_drawdown | 0.2977 |
| cagr | -0.0954 |
| net_avg_win | 75.2267 |
| net_avg_loss | -94.8686 |
| avg_hold_time_bars | 51.8750 |
| exposure | 0.6980 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
