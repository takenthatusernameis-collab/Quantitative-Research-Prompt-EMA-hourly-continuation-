# EMA Hourly Continuation — XLM/USDT P8_26

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1640 |
| net_profit_factor | 0.2365 |
| net_win_rate | 0.4354 |
| gross_profit_factor | 0.8107 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -12.1916 |
| sortino_ratio | -6.9782 |
| max_drawdown | 0.9999 |
| cagr | -0.9717 |
| net_avg_win | 4.3382 |
| net_avg_loss | -14.1427 |
| avg_hold_time_bars | 3.5159 |
| exposure | 0.2621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
