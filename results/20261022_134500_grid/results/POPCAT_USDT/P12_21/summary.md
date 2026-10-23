# EMA Hourly Continuation — POPCAT/USDT P12_21

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1304 |
| net_profit_factor | 0.4251 |
| net_win_rate | 0.4034 |
| gross_profit_factor | 0.6874 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -11.6979 |
| sortino_ratio | -6.4604 |
| max_drawdown | 0.9990 |
| cagr | -0.9589 |
| net_avg_win | 14.0453 |
| net_avg_loss | -22.3364 |
| avg_hold_time_bars | 2.3420 |
| exposure | 0.1613 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
