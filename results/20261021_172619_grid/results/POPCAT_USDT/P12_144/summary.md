# EMA Hourly Continuation — POPCAT/USDT P12_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8134 |
| net_win_rate | 0.4825 |
| gross_profit_factor | 0.9201 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -1.1597 |
| sortino_ratio | -0.3161 |
| max_drawdown | 0.3252 |
| cagr | -0.1374 |
| net_avg_win | 78.4237 |
| net_avg_loss | -89.9085 |
| avg_hold_time_bars | 40.1079 |
| exposure | 0.6674 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
