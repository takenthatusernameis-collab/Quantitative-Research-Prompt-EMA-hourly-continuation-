# EMA Hourly Continuation — API3/USDT P34_144

**Symbol:** API3/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.8262 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -1.2015 |
| sortino_ratio | -0.3440 |
| max_drawdown | 0.4147 |
| cagr | -0.1481 |
| net_avg_win | 78.3411 |
| net_avg_loss | -95.7767 |
| avg_hold_time_bars | 21.5850 |
| exposure | 0.3925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
