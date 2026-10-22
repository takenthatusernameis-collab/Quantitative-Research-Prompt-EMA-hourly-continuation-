# EMA Hourly Continuation — KAS/USDT P89_200

**Symbol:** KAS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.4512 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.7839 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -4.4848 |
| sortino_ratio | -1.3000 |
| max_drawdown | 0.8122 |
| cagr | -0.4751 |
| net_avg_win | 34.1563 |
| net_avg_loss | -61.9100 |
| avg_hold_time_bars | 9.4802 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
