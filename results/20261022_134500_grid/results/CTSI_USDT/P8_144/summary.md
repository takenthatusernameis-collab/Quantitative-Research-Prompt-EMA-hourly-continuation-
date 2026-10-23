# EMA Hourly Continuation — CTSI/USDT P8_144

**Symbol:** CTSI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6747 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -3.3065 |
| sortino_ratio | -1.0502 |
| max_drawdown | 0.7340 |
| cagr | -0.3952 |
| net_avg_win | 62.2460 |
| net_avg_loss | -80.1771 |
| avg_hold_time_bars | 31.5331 |
| exposure | 0.7367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
