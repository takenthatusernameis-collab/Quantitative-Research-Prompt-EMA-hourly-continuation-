# EMA Hourly Continuation — AKT/USDT P50_144

**Symbol:** AKT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.6621 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9711 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -2.7243 |
| sortino_ratio | -0.8719 |
| max_drawdown | 0.6550 |
| cagr | -0.3409 |
| net_avg_win | 49.6712 |
| net_avg_loss | -74.4426 |
| avg_hold_time_bars | 11.4922 |
| exposure | 0.2685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
