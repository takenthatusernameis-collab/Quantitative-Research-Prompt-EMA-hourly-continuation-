# EMA Hourly Continuation — ARB/USDT P26_55

**Symbol:** ARB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.8726 |
| net_win_rate | 0.5401 |
| gross_profit_factor | 1.1580 |
| gross_win_rate | 0.5401 |
| sharpe_ratio | -0.7548 |
| sortino_ratio | -0.2150 |
| max_drawdown | 0.2686 |
| cagr | -0.0967 |
| net_avg_win | 73.8485 |
| net_avg_loss | -99.3745 |
| avg_hold_time_bars | 7.7313 |
| exposure | 0.1360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
