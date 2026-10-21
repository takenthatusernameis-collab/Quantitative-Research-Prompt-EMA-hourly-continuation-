# EMA Hourly Continuation — ZRX/USDT P8_34

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.6384 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8771 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -4.4202 |
| sortino_ratio | -1.8592 |
| max_drawdown | 0.8854 |
| cagr | -0.5737 |
| net_avg_win | 38.4710 |
| net_avg_loss | -52.5982 |
| avg_hold_time_bars | 8.2394 |
| exposure | 0.3255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
