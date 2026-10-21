# EMA Hourly Continuation — AVAX/USDT P12_89

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7942 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9840 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -2.0177 |
| sortino_ratio | -0.6473 |
| max_drawdown | 0.6052 |
| cagr | -0.2591 |
| net_avg_win | 82.9889 |
| net_avg_loss | -98.8727 |
| avg_hold_time_bars | 20.9941 |
| exposure | 0.4829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
