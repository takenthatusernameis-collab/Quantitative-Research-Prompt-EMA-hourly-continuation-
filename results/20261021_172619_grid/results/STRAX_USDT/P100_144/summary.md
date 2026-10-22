# EMA Hourly Continuation — STRAX/USDT P100_144

**Symbol:** STRAX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.4600 |
| net_win_rate | 0.4065 |
| gross_profit_factor | 0.6892 |
| gross_win_rate | 0.4065 |
| sharpe_ratio | -4.3340 |
| sortino_ratio | -1.0900 |
| max_drawdown | 0.7241 |
| cagr | -0.3986 |
| net_avg_win | 48.6077 |
| net_avg_loss | -72.3651 |
| avg_hold_time_bars | 7.6387 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
