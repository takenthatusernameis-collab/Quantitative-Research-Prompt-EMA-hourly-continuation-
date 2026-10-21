# EMA Hourly Continuation — XTZ/USDT P20_200

**Symbol:** XTZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.7817 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -1.3039 |
| sortino_ratio | -0.3259 |
| max_drawdown | 0.3350 |
| cagr | -0.1397 |
| net_avg_win | 74.1142 |
| net_avg_loss | -94.1926 |
| avg_hold_time_bars | 47.6984 |
| exposure | 0.6613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
