# EMA Hourly Continuation — KAVA/USDT P50_200

**Symbol:** KAVA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.6662 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.9154 |
| gross_win_rate | 0.4770 |
| sharpe_ratio | -2.3993 |
| sortino_ratio | -0.5891 |
| max_drawdown | 0.5159 |
| cagr | -0.2439 |
| net_avg_win | 69.9059 |
| net_avg_loss | -94.4412 |
| avg_hold_time_bars | 30.7237 |
| exposure | 0.4245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
