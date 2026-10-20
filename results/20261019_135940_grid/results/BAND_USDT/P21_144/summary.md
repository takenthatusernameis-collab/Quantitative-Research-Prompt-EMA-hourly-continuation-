# EMA Hourly Continuation — BAND/USDT P21_144

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6251 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4749 |
| sharpe_ratio | -3.2717 |
| sortino_ratio | -1.0097 |
| max_drawdown | 0.7063 |
| cagr | -0.3766 |
| net_avg_win | 51.8353 |
| net_avg_loss | -73.1333 |
| avg_hold_time_bars | 25.0774 |
| exposure | 0.5424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
