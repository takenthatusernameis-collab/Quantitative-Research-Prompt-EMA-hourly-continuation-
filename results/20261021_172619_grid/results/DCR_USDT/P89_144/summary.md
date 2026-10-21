# EMA Hourly Continuation — DCR/USDT P89_144

**Symbol:** DCR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8000 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -3.0098 |
| sortino_ratio | -0.7536 |
| max_drawdown | 0.5836 |
| cagr | -0.2934 |
| net_avg_win | 52.1716 |
| net_avg_loss | -77.2929 |
| avg_hold_time_bars | 8.2774 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
