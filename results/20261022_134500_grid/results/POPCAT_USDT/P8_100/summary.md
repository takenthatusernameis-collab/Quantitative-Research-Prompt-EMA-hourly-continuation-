# EMA Hourly Continuation — POPCAT/USDT P8_100

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 544 |
| net_profit_factor | 0.7063 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9439 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -2.9075 |
| sortino_ratio | -1.0210 |
| max_drawdown | 0.6599 |
| cagr | -0.3915 |
| net_avg_win | 60.4129 |
| net_avg_loss | -79.4673 |
| avg_hold_time_bars | 23.6029 |
| exposure | 0.6783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
