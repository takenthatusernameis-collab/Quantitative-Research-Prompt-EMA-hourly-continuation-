# EMA Hourly Continuation — LUNC/USDT P34_144

**Symbol:** LUNC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 570 |
| net_profit_factor | 0.5316 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8942 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -4.2261 |
| sortino_ratio | -1.4139 |
| max_drawdown | 0.8316 |
| cagr | -0.4973 |
| net_avg_win | 34.5606 |
| net_avg_loss | -58.5122 |
| avg_hold_time_bars | 14.1649 |
| exposure | 0.3670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
