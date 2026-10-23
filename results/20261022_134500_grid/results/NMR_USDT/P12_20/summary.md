# EMA Hourly Continuation — NMR/USDT P12_20

**Symbol:** NMR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1518 |
| net_profit_factor | 0.3083 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.8069 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -14.2721 |
| sortino_ratio | -7.9630 |
| max_drawdown | 1.0000 |
| cagr | -0.9842 |
| net_avg_win | 7.5177 |
| net_avg_loss | -15.6299 |
| avg_hold_time_bars | 2.4249 |
| exposure | 0.1673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
