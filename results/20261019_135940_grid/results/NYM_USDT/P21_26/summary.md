# EMA Hourly Continuation — NYM/USDT P21_26

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.0896 |
| net_win_rate | 0.2054 |
| gross_profit_factor | 0.4774 |
| gross_win_rate | 0.2937 |
| sharpe_ratio | -20.0580 |
| sortino_ratio | -10.6762 |
| max_drawdown | 1.0000 |
| cagr | -0.9977 |
| net_avg_win | 4.4556 |
| net_avg_loss | -12.8476 |
| avg_hold_time_bars | 3.0288 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
