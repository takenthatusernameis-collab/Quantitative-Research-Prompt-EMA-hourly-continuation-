# EMA Hourly Continuation — IO/USDT P34_50

**Symbol:** IO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 837 |
| net_profit_factor | 0.4584 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8104 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -7.4185 |
| sortino_ratio | -3.1239 |
| max_drawdown | 0.9754 |
| cagr | -0.7890 |
| net_avg_win | 21.9358 |
| net_avg_loss | -39.0298 |
| avg_hold_time_bars | 2.5544 |
| exposure | 0.1035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
