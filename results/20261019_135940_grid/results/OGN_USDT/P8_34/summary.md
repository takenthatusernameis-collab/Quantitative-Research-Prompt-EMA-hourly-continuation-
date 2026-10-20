# EMA Hourly Continuation — OGN/USDT P8_34

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1310 |
| net_profit_factor | 0.4842 |
| net_win_rate | 0.4382 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -8.8475 |
| sortino_ratio | -4.4978 |
| max_drawdown | 0.9962 |
| cagr | -0.8893 |
| net_avg_win | 16.2922 |
| net_avg_loss | -26.2403 |
| avg_hold_time_bars | 5.9656 |
| exposure | 0.3536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
