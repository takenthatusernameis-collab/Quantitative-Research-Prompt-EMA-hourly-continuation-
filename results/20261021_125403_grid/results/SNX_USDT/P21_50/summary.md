# EMA Hourly Continuation — SNX/USDT P21_50

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.7547 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0040 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -2.0024 |
| sortino_ratio | -0.6502 |
| max_drawdown | 0.5409 |
| cagr | -0.2576 |
| net_avg_win | 63.0017 |
| net_avg_loss | -84.1288 |
| avg_hold_time_bars | 6.7490 |
| exposure | 0.1570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
