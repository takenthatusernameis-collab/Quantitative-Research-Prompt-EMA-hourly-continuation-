# EMA Hourly Continuation — W/USDT P20_50

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.8013 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0100 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.6883 |
| sortino_ratio | -0.5569 |
| max_drawdown | 0.5158 |
| cagr | -0.2267 |
| net_avg_win | 72.3974 |
| net_avg_loss | -90.3476 |
| avg_hold_time_bars | 7.8415 |
| exposure | 0.1889 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
