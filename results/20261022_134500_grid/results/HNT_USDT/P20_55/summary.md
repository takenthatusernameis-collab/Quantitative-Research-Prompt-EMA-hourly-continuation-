# EMA Hourly Continuation — HNT/USDT P20_55

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.5131 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4546 |
| sharpe_ratio | -6.8068 |
| sortino_ratio | -3.0513 |
| max_drawdown | 0.9768 |
| cagr | -0.7721 |
| net_avg_win | 22.5992 |
| net_avg_loss | -35.8474 |
| avg_hold_time_bars | 5.2495 |
| exposure | 0.2420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
