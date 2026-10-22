# EMA Hourly Continuation — CHZ/USDT P20_144

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.7647 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.1205 |
| gross_win_rate | 0.5255 |
| sharpe_ratio | -1.7750 |
| sortino_ratio | -0.5221 |
| max_drawdown | 0.4843 |
| cagr | -0.2198 |
| net_avg_win | 67.9011 |
| net_avg_loss | -93.8685 |
| avg_hold_time_bars | 29.2153 |
| exposure | 0.5737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
