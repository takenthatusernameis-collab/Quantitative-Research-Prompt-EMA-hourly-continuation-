# EMA Hourly Continuation — BTT/USDT P20_34

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.4281 |
| net_win_rate | 0.4116 |
| gross_profit_factor | 0.8034 |
| gross_win_rate | 0.4145 |
| sharpe_ratio | -5.7183 |
| sortino_ratio | -1.5487 |
| max_drawdown | 0.8420 |
| cagr | -0.5181 |
| net_avg_win | 44.2897 |
| net_avg_loss | -72.3650 |
| avg_hold_time_bars | 6.2319 |
| exposure | 0.0977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
