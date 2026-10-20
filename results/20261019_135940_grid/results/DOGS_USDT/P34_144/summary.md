# EMA Hourly Continuation — DOGS/USDT P34_144

**Symbol:** DOGS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.7672 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -2.1390 |
| sortino_ratio | -0.6661 |
| max_drawdown | 0.5733 |
| cagr | -0.2703 |
| net_avg_win | 78.0105 |
| net_avg_loss | -103.1732 |
| avg_hold_time_bars | 19.5351 |
| exposure | 0.4280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
