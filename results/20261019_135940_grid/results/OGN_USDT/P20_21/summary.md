# EMA Hourly Continuation — OGN/USDT P20_21

**Symbol:** OGN/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.1670 |
| net_win_rate | 0.2992 |
| gross_profit_factor | 0.6626 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -17.2498 |
| sortino_ratio | -8.9872 |
| max_drawdown | 1.0000 |
| cagr | -0.9929 |
| net_avg_win | 5.7115 |
| net_avg_loss | -14.6042 |
| avg_hold_time_bars | 2.0870 |
| exposure | 0.1108 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
