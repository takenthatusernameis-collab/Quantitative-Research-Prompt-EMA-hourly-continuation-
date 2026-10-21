# EMA Hourly Continuation — XMR/USDT P20_89

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6473 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8584 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -3.2252 |
| sortino_ratio | -1.0481 |
| max_drawdown | 0.7086 |
| cagr | -0.3814 |
| net_avg_win | 54.0249 |
| net_avg_loss | -69.9472 |
| avg_hold_time_bars | 11.8084 |
| exposure | 0.2802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
