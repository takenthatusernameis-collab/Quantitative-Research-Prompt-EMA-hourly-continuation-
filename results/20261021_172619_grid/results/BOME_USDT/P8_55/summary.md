# EMA Hourly Continuation — BOME/USDT P8_55

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.8280 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -1.4540 |
| sortino_ratio | -0.5328 |
| max_drawdown | 0.4978 |
| cagr | -0.2204 |
| net_avg_win | 68.2429 |
| net_avg_loss | -82.6696 |
| avg_hold_time_bars | 15.0153 |
| exposure | 0.4470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
