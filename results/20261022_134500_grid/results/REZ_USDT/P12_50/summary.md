# EMA Hourly Continuation — REZ/USDT P12_50

**Symbol:** REZ/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.6307 |
| net_win_rate | 0.4669 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -5.2827 |
| sortino_ratio | -2.3840 |
| max_drawdown | 0.9418 |
| cagr | -0.6805 |
| net_avg_win | 34.0337 |
| net_avg_loss | -47.2536 |
| avg_hold_time_bars | 7.8853 |
| exposure | 0.3678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
