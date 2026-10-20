# EMA Hourly Continuation — DEEP/USDT P34_144

**Symbol:** DEEP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8046 |
| net_win_rate | 0.5202 |
| gross_profit_factor | 1.0661 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -1.3008 |
| sortino_ratio | -0.3834 |
| max_drawdown | 0.3174 |
| cagr | -0.1680 |
| net_avg_win | 70.8417 |
| net_avg_loss | -95.4770 |
| avg_hold_time_bars | 21.1734 |
| exposure | 0.4148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
