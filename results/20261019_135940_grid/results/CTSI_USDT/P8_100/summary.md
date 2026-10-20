# EMA Hourly Continuation — CTSI/USDT P8_100

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 714 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 1.0000 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -4.1202 |
| sortino_ratio | -1.5601 |
| max_drawdown | 0.8402 |
| cagr | -0.5170 |
| net_avg_win | 49.5822 |
| net_avg_loss | -65.6653 |
| avg_hold_time_bars | 19.5826 |
| exposure | 0.6355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
