# EMA Hourly Continuation — YGG/USDT P20_26

**Symbol:** YGG/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.5896 |
| net_win_rate | 0.4440 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -2.9243 |
| sortino_ratio | -0.6822 |
| max_drawdown | 0.5741 |
| cagr | -0.2684 |
| net_avg_win | 65.8586 |
| net_avg_loss | -89.2050 |
| avg_hold_time_bars | 4.0522 |
| exposure | 0.0491 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
