# EMA Hourly Continuation — DGB/USDT P89_100

**Symbol:** DGB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 94 |
| net_profit_factor | 0.5804 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.8076 |
| gross_win_rate | 0.4468 |
| sharpe_ratio | -1.6327 |
| sortino_ratio | -0.2257 |
| max_drawdown | 0.2303 |
| cagr | -0.0990 |
| net_avg_win | 75.8485 |
| net_avg_loss | -105.5570 |
| avg_hold_time_bars | 4.5106 |
| exposure | 0.0193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
