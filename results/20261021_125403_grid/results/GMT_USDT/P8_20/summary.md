# EMA Hourly Continuation — GMT/USDT P8_20

**Symbol:** GMT/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.5716 |
| sortino_ratio | -0.8427 |
| max_drawdown | 0.6357 |
| cagr | -0.3193 |
| net_avg_win | 45.2168 |
| net_avg_loss | -67.4775 |
| avg_hold_time_bars | 5.3090 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
