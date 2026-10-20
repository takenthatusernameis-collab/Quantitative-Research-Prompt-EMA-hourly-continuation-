# EMA Hourly Continuation — YFI/USDT P20_100

**Symbol:** YFI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.4820 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -6.4291 |
| sortino_ratio | -2.4420 |
| max_drawdown | 0.9558 |
| cagr | -0.7054 |
| net_avg_win | 27.1506 |
| net_avg_loss | -44.1722 |
| avg_hold_time_bars | 13.0040 |
| exposure | 0.4378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
