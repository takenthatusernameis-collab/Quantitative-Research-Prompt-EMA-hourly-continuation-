# EMA Hourly Continuation — GLM/USDT P34_55

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 828 |
| net_profit_factor | 0.3519 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.7667 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -7.2683 |
| sortino_ratio | -2.9565 |
| max_drawdown | 0.9746 |
| cagr | -0.7682 |
| net_avg_win | 13.8547 |
| net_avg_loss | -33.7176 |
| avg_hold_time_bars | 4.0072 |
| exposure | 0.1508 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
