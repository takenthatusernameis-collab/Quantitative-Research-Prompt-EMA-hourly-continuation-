# EMA Hourly Continuation — SHIB/USDT P12_20

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.6825 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 1.0115 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.9500 |
| sortino_ratio | -0.4321 |
| max_drawdown | 0.4090 |
| cagr | -0.1792 |
| net_avg_win | 71.2401 |
| net_avg_loss | -103.5003 |
| avg_hold_time_bars | 4.5654 |
| exposure | 0.0492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
