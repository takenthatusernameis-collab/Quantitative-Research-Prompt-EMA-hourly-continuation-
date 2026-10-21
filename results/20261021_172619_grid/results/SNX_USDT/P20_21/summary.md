# EMA Hourly Continuation — SNX/USDT P20_21

**Symbol:** SNX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.7137 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0392 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.2696 |
| sortino_ratio | -0.2244 |
| max_drawdown | 0.2881 |
| cagr | -0.0965 |
| net_avg_win | 73.1397 |
| net_avg_loss | -106.6291 |
| avg_hold_time_bars | 4.4172 |
| exposure | 0.0302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
