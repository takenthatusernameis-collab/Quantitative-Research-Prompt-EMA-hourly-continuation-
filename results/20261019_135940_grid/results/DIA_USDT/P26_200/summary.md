# EMA Hourly Continuation — DIA/USDT P26_200

**Symbol:** DIA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7290 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0496 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -1.6950 |
| sortino_ratio | -0.4690 |
| max_drawdown | 0.5573 |
| cagr | -0.2015 |
| net_avg_win | 58.2708 |
| net_avg_loss | -85.4874 |
| avg_hold_time_bars | 32.9173 |
| exposure | 0.5765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
