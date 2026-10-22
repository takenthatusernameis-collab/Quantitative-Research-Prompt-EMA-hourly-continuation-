# EMA Hourly Continuation — MOG/USDT P8_50

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.8309 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -1.5943 |
| sortino_ratio | -0.5884 |
| max_drawdown | 0.4964 |
| cagr | -0.2398 |
| net_avg_win | 76.2676 |
| net_avg_loss | -89.4095 |
| avg_hold_time_bars | 14.6246 |
| exposure | 0.4435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
