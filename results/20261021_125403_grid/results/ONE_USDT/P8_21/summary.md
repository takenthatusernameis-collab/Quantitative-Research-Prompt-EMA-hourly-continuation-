# EMA Hourly Continuation — ONE/USDT P8_21

**Symbol:** ONE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.8044 |
| net_win_rate | 0.5211 |
| gross_profit_factor | 1.0723 |
| gross_win_rate | 0.5211 |
| sharpe_ratio | -1.5020 |
| sortino_ratio | -0.5053 |
| max_drawdown | 0.4699 |
| cagr | -0.2079 |
| net_avg_win | 64.1391 |
| net_avg_loss | -86.7642 |
| avg_hold_time_bars | 6.3339 |
| exposure | 0.1569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
