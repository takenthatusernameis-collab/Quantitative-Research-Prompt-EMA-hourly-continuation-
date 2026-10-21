# EMA Hourly Continuation — RPL/USDT P8_20

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 761 |
| net_profit_factor | 0.7932 |
| net_win_rate | 0.5204 |
| gross_profit_factor | 1.1313 |
| gross_win_rate | 0.5204 |
| sharpe_ratio | -2.4232 |
| sortino_ratio | -0.9604 |
| max_drawdown | 0.7076 |
| cagr | -0.3567 |
| net_avg_win | 65.0377 |
| net_avg_loss | -88.9546 |
| avg_hold_time_bars | 5.8187 |
| exposure | 0.2004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
