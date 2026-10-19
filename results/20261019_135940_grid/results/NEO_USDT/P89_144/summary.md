# EMA Hourly Continuation — NEO/USDT P89_144

**Symbol:** NEO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.4317 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -6.1121 |
| sortino_ratio | -2.0262 |
| max_drawdown | 0.9210 |
| cagr | -0.6334 |
| net_avg_win | 28.6233 |
| net_avg_loss | -53.0484 |
| avg_hold_time_bars | 4.5027 |
| exposure | 0.1124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
