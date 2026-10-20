# EMA Hourly Continuation — RLC/USDT P8_100

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7692 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.1332 |
| gross_win_rate | 0.5263 |
| sharpe_ratio | -2.1656 |
| sortino_ratio | -0.7142 |
| max_drawdown | 0.6563 |
| cagr | -0.2913 |
| net_avg_win | 68.6538 |
| net_avg_loss | -92.8893 |
| avg_hold_time_bars | 28.6733 |
| exposure | 0.7181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
