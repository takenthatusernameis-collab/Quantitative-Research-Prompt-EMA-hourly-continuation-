# EMA Hourly Continuation — SQD/USDT P8_12

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.7740 |
| net_win_rate | 0.5059 |
| gross_profit_factor | 1.0012 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -1.1732 |
| sortino_ratio | -0.2735 |
| max_drawdown | 0.3193 |
| cagr | -0.1178 |
| net_avg_win | 69.7008 |
| net_avg_loss | -92.1925 |
| avg_hold_time_bars | 5.0196 |
| exposure | 0.0602 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
