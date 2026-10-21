# EMA Hourly Continuation — SEI/USDT P8_55

**Symbol:** SEI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.8399 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0302 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -1.4441 |
| sortino_ratio | -0.5184 |
| max_drawdown | 0.5139 |
| cagr | -0.2144 |
| net_avg_win | 75.1896 |
| net_avg_loss | -91.8437 |
| avg_hold_time_bars | 16.7157 |
| exposure | 0.4756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
