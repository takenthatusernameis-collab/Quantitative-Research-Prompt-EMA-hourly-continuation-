# EMA Hourly Continuation — UNI/USDT P8_26

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.7326 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9832 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -2.2987 |
| sortino_ratio | -0.7968 |
| max_drawdown | 0.5990 |
| cagr | -0.3049 |
| net_avg_win | 56.5833 |
| net_avg_loss | -76.1806 |
| avg_hold_time_bars | 6.7295 |
| exposure | 0.1786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
