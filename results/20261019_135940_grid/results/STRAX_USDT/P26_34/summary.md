# EMA Hourly Continuation — STRAX/USDT P26_34

**Symbol:** STRAX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1071 |
| net_profit_factor | 0.3734 |
| net_win_rate | 0.3819 |
| gross_profit_factor | 0.9188 |
| gross_win_rate | 0.4332 |
| sharpe_ratio | -12.1790 |
| sortino_ratio | -5.6789 |
| max_drawdown | 0.9995 |
| cagr | -0.9505 |
| net_avg_win | 14.5600 |
| net_avg_loss | -24.0930 |
| avg_hold_time_bars | 3.6844 |
| exposure | 0.1804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
