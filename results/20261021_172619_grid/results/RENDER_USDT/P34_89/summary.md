# EMA Hourly Continuation — RENDER/USDT P34_89

**Symbol:** RENDER/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.7454 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9350 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -1.9981 |
| sortino_ratio | -0.6114 |
| max_drawdown | 0.5120 |
| cagr | -0.2454 |
| net_avg_win | 69.5502 |
| net_avg_loss | -87.8166 |
| avg_hold_time_bars | 9.6061 |
| exposure | 0.2008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
