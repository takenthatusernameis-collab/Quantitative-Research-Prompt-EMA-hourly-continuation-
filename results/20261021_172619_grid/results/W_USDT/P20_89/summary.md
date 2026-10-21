# EMA Hourly Continuation — W/USDT P20_89

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.8402 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0147 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.1989 |
| sortino_ratio | -0.3798 |
| max_drawdown | 0.4113 |
| cagr | -0.1627 |
| net_avg_win | 76.5631 |
| net_avg_loss | -93.0114 |
| avg_hold_time_bars | 16.6319 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
