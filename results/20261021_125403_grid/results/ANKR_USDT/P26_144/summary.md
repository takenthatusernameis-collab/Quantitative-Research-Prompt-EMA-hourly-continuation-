# EMA Hourly Continuation — ANKR/USDT P26_144

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.7048 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8993 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.4918 |
| sortino_ratio | -0.7185 |
| max_drawdown | 0.5733 |
| cagr | -0.2831 |
| net_avg_win | 70.8233 |
| net_avg_loss | -87.2354 |
| avg_hold_time_bars | 26.5304 |
| exposure | 0.4956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
