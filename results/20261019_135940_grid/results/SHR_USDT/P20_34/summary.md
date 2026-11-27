# EMA Hourly Continuation — SHR/USDT P20_34

**Symbol:** SHR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1342 |
| net_profit_factor | 0.3116 |
| net_win_rate | 0.2876 |
| gross_profit_factor | 0.5625 |
| gross_win_rate | 0.2921 |
| sharpe_ratio | -15.1355 |
| sortino_ratio | -7.8438 |
| max_drawdown | 1.0000 |
| cagr | -0.9810 |
| net_avg_win | 11.7269 |
| net_avg_loss | -15.1947 |
| avg_hold_time_bars | 2.8174 |
| exposure | 0.1711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
