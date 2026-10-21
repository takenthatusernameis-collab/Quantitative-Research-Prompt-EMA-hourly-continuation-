# EMA Hourly Continuation — SOL/USDT P50_144

**Symbol:** SOL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6983 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.1067 |
| sortino_ratio | -0.5571 |
| max_drawdown | 0.5154 |
| cagr | -0.2262 |
| net_avg_win | 66.6176 |
| net_avg_loss | -88.4268 |
| avg_hold_time_bars | 13.9504 |
| exposure | 0.2175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
