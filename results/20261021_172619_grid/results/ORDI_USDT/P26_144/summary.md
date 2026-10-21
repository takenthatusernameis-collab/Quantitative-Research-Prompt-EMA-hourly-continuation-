# EMA Hourly Continuation — ORDI/USDT P26_144

**Symbol:** ORDI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7333 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.0572 |
| sortino_ratio | -0.5925 |
| max_drawdown | 0.5155 |
| cagr | -0.2390 |
| net_avg_win | 71.4464 |
| net_avg_loss | -84.5905 |
| avg_hold_time_bars | 21.9586 |
| exposure | 0.4102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
