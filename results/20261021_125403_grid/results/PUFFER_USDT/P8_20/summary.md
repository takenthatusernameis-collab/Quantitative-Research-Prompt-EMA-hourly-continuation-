# EMA Hourly Continuation — PUFFER/USDT P8_20

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6694 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.8795 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -2.9801 |
| sortino_ratio | -0.9974 |
| max_drawdown | 0.6388 |
| cagr | -0.3684 |
| net_avg_win | 58.8312 |
| net_avg_loss | -77.7842 |
| avg_hold_time_bars | 7.0045 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
