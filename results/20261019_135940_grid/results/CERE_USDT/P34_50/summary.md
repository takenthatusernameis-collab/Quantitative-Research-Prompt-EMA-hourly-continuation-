# EMA Hourly Continuation — CERE/USDT P34_50

**Symbol:** CERE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.2971 |
| net_win_rate | 0.2784 |
| gross_profit_factor | 0.7202 |
| gross_win_rate | 0.3330 |
| sharpe_ratio | -14.6925 |
| sortino_ratio | -6.5510 |
| max_drawdown | 0.9999 |
| cagr | -0.9731 |
| net_avg_win | 16.5727 |
| net_avg_loss | -21.5203 |
| avg_hold_time_bars | 4.8581 |
| exposure | 0.2023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
