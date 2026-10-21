# EMA Hourly Continuation — KMNO/USDT P8_89

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.8251 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0007 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.4039 |
| sortino_ratio | -0.4418 |
| max_drawdown | 0.4023 |
| cagr | -0.1866 |
| net_avg_win | 78.9504 |
| net_avg_loss | -95.6847 |
| avg_hold_time_bars | 28.1946 |
| exposure | 0.6222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
