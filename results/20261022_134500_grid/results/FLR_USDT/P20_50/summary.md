# EMA Hourly Continuation — FLR/USDT P20_50

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.4413 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.9009 |
| gross_win_rate | 0.4394 |
| sharpe_ratio | -10.5063 |
| sortino_ratio | -5.1239 |
| max_drawdown | 0.9985 |
| cagr | -0.9241 |
| net_avg_win | 16.0320 |
| net_avg_loss | -25.6786 |
| avg_hold_time_bars | 4.1574 |
| exposure | 0.2245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
