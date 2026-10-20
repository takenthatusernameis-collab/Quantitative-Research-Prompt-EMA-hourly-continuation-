# EMA Hourly Continuation — NMR/USDT P20_26

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1279 |
| net_profit_factor | 0.2866 |
| net_win_rate | 0.3612 |
| gross_profit_factor | 0.7442 |
| gross_win_rate | 0.4246 |
| sharpe_ratio | -14.6613 |
| sortino_ratio | -7.5991 |
| max_drawdown | 1.0000 |
| cagr | -0.9828 |
| net_avg_win | 8.6965 |
| net_avg_loss | -17.1572 |
| avg_hold_time_bars | 2.3034 |
| exposure | 0.1339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
