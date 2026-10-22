# EMA Hourly Continuation — JST/USDT P8_26

**Symbol:** JST/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1281 |
| net_profit_factor | 0.1603 |
| net_win_rate | 0.4005 |
| gross_profit_factor | 0.6863 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -13.4016 |
| sortino_ratio | -6.8534 |
| max_drawdown | 0.9999 |
| cagr | -0.9742 |
| net_avg_win | 3.7217 |
| net_avg_loss | -15.5055 |
| avg_hold_time_bars | 4.7674 |
| exposure | 0.2763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
