# EMA Hourly Continuation — XDC/USDT P8_50

**Symbol:** XDC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -3.9999 |
| sortino_ratio | -1.4741 |
| max_drawdown | 0.8178 |
| cagr | -0.4911 |
| net_avg_win | 41.1791 |
| net_avg_loss | -60.3951 |
| avg_hold_time_bars | 11.6872 |
| exposure | 0.3533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
