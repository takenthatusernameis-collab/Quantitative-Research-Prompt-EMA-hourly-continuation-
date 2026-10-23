# EMA Hourly Continuation — LPT/USDT P8_144

**Symbol:** LPT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6638 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.9067 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -3.4025 |
| sortino_ratio | -1.1060 |
| max_drawdown | 0.7427 |
| cagr | -0.4043 |
| net_avg_win | 58.8725 |
| net_avg_loss | -75.4074 |
| avg_hold_time_bars | 29.9134 |
| exposure | 0.7220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
