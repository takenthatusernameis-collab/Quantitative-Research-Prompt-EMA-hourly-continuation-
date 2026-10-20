# EMA Hourly Continuation — ONE/USDT P26_34

**Symbol:** ONE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1151 |
| net_profit_factor | 0.3109 |
| net_win_rate | 0.3858 |
| gross_profit_factor | 0.7688 |
| gross_win_rate | 0.4188 |
| sharpe_ratio | -12.5761 |
| sortino_ratio | -6.1391 |
| max_drawdown | 0.9997 |
| cagr | -0.9594 |
| net_avg_win | 10.1587 |
| net_avg_loss | -20.5194 |
| avg_hold_time_bars | 2.0426 |
| exposure | 0.1069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
