# EMA Hourly Continuation — MERL/USDT P8_89

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 1.0523 |
| gross_win_rate | 0.5075 |
| sharpe_ratio | -2.0856 |
| sortino_ratio | -0.7629 |
| max_drawdown | 0.6615 |
| cagr | -0.3058 |
| net_avg_win | 69.6613 |
| net_avg_loss | -88.4901 |
| avg_hold_time_bars | 21.8403 |
| exposure | 0.6670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
