# EMA Hourly Continuation — EDU/USDT P8_100

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7630 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9242 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -2.0302 |
| sortino_ratio | -0.6769 |
| max_drawdown | 0.5621 |
| cagr | -0.2689 |
| net_avg_win | 66.5816 |
| net_avg_loss | -80.2749 |
| avg_hold_time_bars | 26.4011 |
| exposure | 0.6583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
