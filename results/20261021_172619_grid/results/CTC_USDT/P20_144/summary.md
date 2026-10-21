# EMA Hourly Continuation — CTC/USDT P20_144

**Symbol:** CTC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.8658 |
| net_win_rate | 0.5254 |
| gross_profit_factor | 1.0920 |
| gross_win_rate | 0.5254 |
| sharpe_ratio | -0.8665 |
| sortino_ratio | -0.2530 |
| max_drawdown | 0.3785 |
| cagr | -0.1135 |
| net_avg_win | 77.6026 |
| net_avg_loss | -99.2335 |
| avg_hold_time_bars | 28.3148 |
| exposure | 0.5315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
