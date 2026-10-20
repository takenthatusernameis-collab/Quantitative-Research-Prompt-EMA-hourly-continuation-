# EMA Hourly Continuation — DBR/USDT P89_144

**Symbol:** DBR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.3926 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7536 |
| gross_win_rate | 0.4303 |
| sharpe_ratio | -5.7739 |
| sortino_ratio | -1.6708 |
| max_drawdown | 0.8127 |
| cagr | -0.5641 |
| net_avg_win | 37.1855 |
| net_avg_loss | -68.1375 |
| avg_hold_time_bars | 10.8309 |
| exposure | 0.2076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
