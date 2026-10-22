# EMA Hourly Continuation — CRV/USDT P26_34

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1081 |
| net_profit_factor | 0.3285 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.8182 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -10.4523 |
| sortino_ratio | -4.9010 |
| max_drawdown | 0.9982 |
| cagr | -0.9184 |
| net_avg_win | 10.5709 |
| net_avg_loss | -24.0150 |
| avg_hold_time_bars | 1.9010 |
| exposure | 0.0934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
