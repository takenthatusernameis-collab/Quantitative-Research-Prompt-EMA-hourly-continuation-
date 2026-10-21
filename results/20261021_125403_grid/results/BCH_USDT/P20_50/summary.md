# EMA Hourly Continuation — BCH/USDT P20_50

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.6500 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9441 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -3.0818 |
| sortino_ratio | -0.9419 |
| max_drawdown | 0.6631 |
| cagr | -0.3499 |
| net_avg_win | 56.3090 |
| net_avg_loss | -79.6814 |
| avg_hold_time_bars | 9.3231 |
| exposure | 0.1928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
