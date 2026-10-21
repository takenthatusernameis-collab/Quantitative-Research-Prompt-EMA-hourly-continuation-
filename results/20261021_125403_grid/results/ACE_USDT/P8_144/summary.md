# EMA Hourly Continuation — ACE/USDT P8_144

**Symbol:** ACE/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.8325 |
| net_win_rate | 0.4944 |
| gross_profit_factor | 0.9811 |
| gross_win_rate | 0.4944 |
| sharpe_ratio | -1.0009 |
| sortino_ratio | -0.2334 |
| max_drawdown | 0.3544 |
| cagr | -0.1034 |
| net_avg_win | 89.9124 |
| net_avg_loss | -105.6223 |
| avg_hold_time_bars | 63.5762 |
| exposure | 0.7739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
