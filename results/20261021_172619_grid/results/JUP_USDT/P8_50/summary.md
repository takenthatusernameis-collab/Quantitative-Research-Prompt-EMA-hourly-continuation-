# EMA Hourly Continuation — JUP/USDT P8_50

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.8185 |
| net_win_rate | 0.4949 |
| gross_profit_factor | 0.9967 |
| gross_win_rate | 0.4949 |
| sharpe_ratio | -1.8316 |
| sortino_ratio | -0.6867 |
| max_drawdown | 0.5771 |
| cagr | -0.2722 |
| net_avg_win | 72.9158 |
| net_avg_loss | -87.2860 |
| avg_hold_time_bars | 13.2547 |
| exposure | 0.4139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
