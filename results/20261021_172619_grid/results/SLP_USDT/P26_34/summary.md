# EMA Hourly Continuation — SLP/USDT P26_34

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.7161 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0538 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.8630 |
| sortino_ratio | -0.4102 |
| max_drawdown | 0.4806 |
| cagr | -0.1711 |
| net_avg_win | 81.0307 |
| net_avg_loss | -113.1555 |
| avg_hold_time_bars | 4.4915 |
| exposure | 0.0478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
