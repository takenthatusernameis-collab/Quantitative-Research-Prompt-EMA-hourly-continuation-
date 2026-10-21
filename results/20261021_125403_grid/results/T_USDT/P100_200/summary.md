# EMA Hourly Continuation — T/USDT P100_200

**Symbol:** T/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7828 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1053 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -1.3113 |
| sortino_ratio | -0.3322 |
| max_drawdown | 0.3472 |
| cagr | -0.1420 |
| net_avg_win | 70.4208 |
| net_avg_loss | -100.3683 |
| avg_hold_time_bars | 13.2765 |
| exposure | 0.1868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
