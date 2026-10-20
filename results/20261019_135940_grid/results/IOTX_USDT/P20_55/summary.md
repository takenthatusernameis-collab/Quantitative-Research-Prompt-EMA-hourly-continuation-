# EMA Hourly Continuation — IOTX/USDT P20_55

**Symbol:** IOTX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 984 |
| net_profit_factor | 0.5753 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.4817 |
| sharpe_ratio | -6.5608 |
| sortino_ratio | -2.9047 |
| max_drawdown | 0.9719 |
| cagr | -0.7546 |
| net_avg_win | 28.6425 |
| net_avg_loss | -43.5300 |
| avg_hold_time_bars | 5.0793 |
| exposure | 0.2272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
