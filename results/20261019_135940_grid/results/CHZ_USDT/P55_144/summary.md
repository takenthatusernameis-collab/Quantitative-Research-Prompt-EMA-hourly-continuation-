# EMA Hourly Continuation — CHZ/USDT P55_144

**Symbol:** CHZ/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6025 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -3.5176 |
| sortino_ratio | -1.0919 |
| max_drawdown | 0.7315 |
| cagr | -0.3990 |
| net_avg_win | 49.2711 |
| net_avg_loss | -70.9143 |
| avg_hold_time_bars | 11.3849 |
| exposure | 0.2474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
