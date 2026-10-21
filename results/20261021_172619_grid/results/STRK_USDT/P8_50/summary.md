# EMA Hourly Continuation — STRK/USDT P8_50

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7910 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9660 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.9773 |
| sortino_ratio | -0.7311 |
| max_drawdown | 0.5816 |
| cagr | -0.2866 |
| net_avg_win | 65.9882 |
| net_avg_loss | -80.0067 |
| avg_hold_time_bars | 13.4179 |
| exposure | 0.4086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
