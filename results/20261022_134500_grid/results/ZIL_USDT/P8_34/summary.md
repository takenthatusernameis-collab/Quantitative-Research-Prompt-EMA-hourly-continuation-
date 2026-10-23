# EMA Hourly Continuation — ZIL/USDT P8_34

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1372 |
| net_profit_factor | 0.4108 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -8.8058 |
| sortino_ratio | -4.5858 |
| max_drawdown | 0.9969 |
| cagr | -0.8969 |
| net_avg_win | 11.1919 |
| net_avg_loss | -22.5258 |
| avg_hold_time_bars | 5.5000 |
| exposure | 0.3430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
