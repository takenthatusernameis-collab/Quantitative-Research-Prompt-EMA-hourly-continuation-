# EMA Hourly Continuation — XDC/USDT P8_89

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.3433 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.8298 |
| gross_win_rate | 0.4784 |
| sharpe_ratio | -7.5484 |
| sortino_ratio | -3.1857 |
| max_drawdown | 0.9839 |
| cagr | -0.8052 |
| net_avg_win | 12.4809 |
| net_avg_loss | -29.1394 |
| avg_hold_time_bars | 12.5497 |
| exposure | 0.5282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
