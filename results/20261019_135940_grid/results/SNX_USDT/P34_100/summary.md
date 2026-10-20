# EMA Hourly Continuation — SNX/USDT P34_100

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 665 |
| net_profit_factor | 0.6762 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0670 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -3.9371 |
| sortino_ratio | -1.4194 |
| max_drawdown | 0.8297 |
| cagr | -0.4994 |
| net_avg_win | 52.5488 |
| net_avg_loss | -75.6402 |
| avg_hold_time_bars | 8.8902 |
| exposure | 0.2675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
