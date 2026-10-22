# EMA Hourly Continuation — SNX/USDT P26_50

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 969 |
| net_profit_factor | 0.5543 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 1.0313 |
| gross_win_rate | 0.4995 |
| sharpe_ratio | -6.2811 |
| sortino_ratio | -2.7702 |
| max_drawdown | 0.9660 |
| cagr | -0.7358 |
| net_avg_win | 25.5987 |
| net_avg_loss | -43.3151 |
| avg_hold_time_bars | 3.4345 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
