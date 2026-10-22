# EMA Hourly Continuation — BOSON/USDT P8_20

**Symbol:** BOSON/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1392 |
| net_profit_factor | 0.4266 |
| net_win_rate | 0.4181 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -10.0502 |
| sortino_ratio | -5.2539 |
| max_drawdown | 0.9986 |
| cagr | -0.9262 |
| net_avg_win | 12.7651 |
| net_avg_loss | -21.4999 |
| avg_hold_time_bars | 3.7802 |
| exposure | 0.2392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
