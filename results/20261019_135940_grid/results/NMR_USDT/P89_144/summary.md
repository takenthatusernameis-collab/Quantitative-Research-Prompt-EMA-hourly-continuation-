# EMA Hourly Continuation — NMR/USDT P89_144

**Symbol:** NMR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.4898 |
| net_win_rate | 0.4402 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.7565 |
| sortino_ratio | -1.8607 |
| max_drawdown | 0.9079 |
| cagr | -0.6047 |
| net_avg_win | 37.3583 |
| net_avg_loss | -59.9833 |
| avg_hold_time_bars | 5.7078 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
