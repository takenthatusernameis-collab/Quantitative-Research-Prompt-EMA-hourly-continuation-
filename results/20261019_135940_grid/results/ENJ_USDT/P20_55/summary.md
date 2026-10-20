# EMA Hourly Continuation — ENJ/USDT P20_55

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.5054 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -7.3261 |
| sortino_ratio | -3.2060 |
| max_drawdown | 0.9814 |
| cagr | -0.7918 |
| net_avg_win | 23.5179 |
| net_avg_loss | -36.9166 |
| avg_hold_time_bars | 5.1828 |
| exposure | 0.2269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
