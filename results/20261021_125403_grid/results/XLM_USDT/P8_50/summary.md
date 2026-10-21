# EMA Hourly Continuation — XLM/USDT P8_50

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 701 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.5007 |
| gross_profit_factor | 0.9830 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -2.6068 |
| sortino_ratio | -0.9896 |
| max_drawdown | 0.6857 |
| cagr | -0.3650 |
| net_avg_win | 46.2600 |
| net_avg_loss | -65.8317 |
| avg_hold_time_bars | 13.1912 |
| exposure | 0.4203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
