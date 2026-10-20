# EMA Hourly Continuation — NMR/USDT P26_55

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 980 |
| net_profit_factor | 0.5513 |
| net_win_rate | 0.4500 |
| gross_profit_factor | 0.9664 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -7.4775 |
| sortino_ratio | -3.2825 |
| max_drawdown | 0.9836 |
| cagr | -0.8032 |
| net_avg_win | 27.3906 |
| net_avg_loss | -40.6505 |
| avg_hold_time_bars | 4.5816 |
| exposure | 0.2041 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
