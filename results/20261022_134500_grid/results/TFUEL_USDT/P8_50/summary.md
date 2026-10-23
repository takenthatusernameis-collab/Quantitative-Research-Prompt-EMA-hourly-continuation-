# EMA Hourly Continuation — TFUEL/USDT P8_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1369 |
| net_profit_factor | 0.5226 |
| net_win_rate | 0.4076 |
| gross_profit_factor | 0.8572 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -10.1320 |
| sortino_ratio | -5.2402 |
| max_drawdown | 0.9986 |
| cagr | -0.9260 |
| net_avg_win | 19.5891 |
| net_avg_loss | -25.7912 |
| avg_hold_time_bars | 6.6786 |
| exposure | 0.4137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
