# EMA Hourly Continuation — GMT/USDT P20_26

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.5646 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -2.4272 |
| sortino_ratio | -0.5035 |
| max_drawdown | 0.4436 |
| cagr | -0.2063 |
| net_avg_win | 59.4708 |
| net_avg_loss | -88.7007 |
| avg_hold_time_bars | 4.0476 |
| exposure | 0.0386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
