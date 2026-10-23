# EMA Hourly Continuation — TRADE/USDT P12_144

**Symbol:** TRADE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.6679 |
| net_win_rate | 0.4648 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4648 |
| sharpe_ratio | -2.5250 |
| sortino_ratio | -0.7347 |
| max_drawdown | 0.6149 |
| cagr | -0.2942 |
| net_avg_win | 59.2338 |
| net_avg_loss | -77.0130 |
| avg_hold_time_bars | 32.3897 |
| exposure | 0.6272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
