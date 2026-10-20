# EMA Hourly Continuation — GMT/USDT P34_100

**Symbol:** GMT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.5567 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4578 |
| sharpe_ratio | -5.3069 |
| sortino_ratio | -1.9097 |
| max_drawdown | 0.9060 |
| cagr | -0.6020 |
| net_avg_win | 38.7513 |
| net_avg_loss | -56.6190 |
| avg_hold_time_bars | 9.1306 |
| exposure | 0.2702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
