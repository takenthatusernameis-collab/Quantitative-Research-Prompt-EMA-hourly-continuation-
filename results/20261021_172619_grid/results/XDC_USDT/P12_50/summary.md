# EMA Hourly Continuation — XDC/USDT P12_50

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6022 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -3.8233 |
| sortino_ratio | -1.3000 |
| max_drawdown | 0.7766 |
| cagr | -0.4483 |
| net_avg_win | 44.1331 |
| net_avg_loss | -65.1958 |
| avg_hold_time_bars | 10.1735 |
| exposure | 0.2613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
