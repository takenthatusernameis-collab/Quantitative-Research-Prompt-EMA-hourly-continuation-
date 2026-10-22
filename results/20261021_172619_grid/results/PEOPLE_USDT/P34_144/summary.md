# EMA Hourly Continuation — PEOPLE/USDT P34_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.9316 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1135 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.3628 |
| sortino_ratio | -0.0980 |
| max_drawdown | 0.2184 |
| cagr | -0.0485 |
| net_avg_win | 86.1817 |
| net_avg_loss | -103.6586 |
| avg_hold_time_bars | 26.0170 |
| exposure | 0.4144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
