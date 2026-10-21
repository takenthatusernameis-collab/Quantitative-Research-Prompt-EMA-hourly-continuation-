# EMA Hourly Continuation — CTSI/USDT P8_144

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.8014 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9797 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.5859 |
| sortino_ratio | -0.4576 |
| max_drawdown | 0.4796 |
| cagr | -0.1907 |
| net_avg_win | 83.6097 |
| net_avg_loss | -98.8587 |
| avg_hold_time_bars | 39.1002 |
| exposure | 0.7269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
