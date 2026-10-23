# EMA Hourly Continuation — CARV/USDT P100_144

**Symbol:** CARV/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.4262 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8193 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -5.0112 |
| sortino_ratio | -1.4838 |
| max_drawdown | 0.7764 |
| cagr | -0.5182 |
| net_avg_win | 35.6406 |
| net_avg_loss | -68.0030 |
| avg_hold_time_bars | 5.1448 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
