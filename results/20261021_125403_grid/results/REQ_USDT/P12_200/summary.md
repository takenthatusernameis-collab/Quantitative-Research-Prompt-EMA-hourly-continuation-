# EMA Hourly Continuation — REQ/USDT P12_200

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.5815 |
| net_win_rate | 0.4196 |
| gross_profit_factor | 0.7787 |
| gross_win_rate | 0.4238 |
| sharpe_ratio | -4.2600 |
| sortino_ratio | -1.3208 |
| max_drawdown | 0.7863 |
| cagr | -0.4591 |
| net_avg_win | 54.3658 |
| net_avg_loss | -67.5930 |
| avg_hold_time_bars | 27.8852 |
| exposure | 0.6071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
