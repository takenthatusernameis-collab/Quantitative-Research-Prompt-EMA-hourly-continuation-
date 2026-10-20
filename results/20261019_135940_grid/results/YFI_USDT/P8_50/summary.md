# EMA Hourly Continuation — YFI/USDT P8_50

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1294 |
| net_profit_factor | 0.4086 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8595 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -9.6502 |
| sortino_ratio | -4.8814 |
| max_drawdown | 0.9979 |
| cagr | -0.9113 |
| net_avg_win | 12.4215 |
| net_avg_loss | -22.8305 |
| avg_hold_time_bars | 7.5873 |
| exposure | 0.4443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
