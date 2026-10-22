# EMA Hourly Continuation — BNB/USDT P12_21

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1467 |
| net_profit_factor | 0.1320 |
| net_win_rate | 0.3013 |
| gross_profit_factor | 0.6394 |
| gross_win_rate | 0.4329 |
| sharpe_ratio | -19.5873 |
| sortino_ratio | -11.4990 |
| max_drawdown | 1.0000 |
| cagr | -0.9982 |
| net_avg_win | 3.4397 |
| net_avg_loss | -11.2394 |
| avg_hold_time_bars | 2.2181 |
| exposure | 0.1479 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
