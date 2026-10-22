# EMA Hourly Continuation — ICP/USDT P20_34

**Symbol:** ICP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1180 |
| net_profit_factor | 0.3510 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.8205 |
| gross_win_rate | 0.4432 |
| sharpe_ratio | -11.1643 |
| sortino_ratio | -5.4485 |
| max_drawdown | 0.9991 |
| cagr | -0.9391 |
| net_avg_win | 11.0067 |
| net_avg_loss | -22.3446 |
| avg_hold_time_bars | 2.4881 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
