# EMA Hourly Continuation — UQC/USDT P20_55

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.1550 |
| net_win_rate | 0.2749 |
| gross_profit_factor | 0.3857 |
| gross_win_rate | 0.2968 |
| sharpe_ratio | -8.7194 |
| sortino_ratio | -2.5110 |
| max_drawdown | 0.9648 |
| cagr | -0.7346 |
| net_avg_win | 15.6572 |
| net_avg_loss | -38.3112 |
| avg_hold_time_bars | 29.3674 |
| exposure | 0.5463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
