# EMA Hourly Continuation — ONE/USDT P20_144

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8509 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0008 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9999 |
| sortino_ratio | -0.2666 |
| max_drawdown | 0.3725 |
| cagr | -0.1176 |
| net_avg_win | 88.4702 |
| net_avg_loss | -103.9674 |
| avg_hold_time_bars | 37.0460 |
| exposure | 0.5860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
