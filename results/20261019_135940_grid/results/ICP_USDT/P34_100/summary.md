# EMA Hourly Continuation — ICP/USDT P34_100

**Symbol:** ICP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.5463 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -5.0053 |
| sortino_ratio | -1.8339 |
| max_drawdown | 0.8929 |
| cagr | -0.5856 |
| net_avg_win | 34.4768 |
| net_avg_loss | -53.4816 |
| avg_hold_time_bars | 8.3186 |
| exposure | 0.2564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
