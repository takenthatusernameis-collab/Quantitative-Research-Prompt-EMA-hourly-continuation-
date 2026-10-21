# EMA Hourly Continuation — QNT/USDT P34_55

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.5969 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.8858 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.6016 |
| sortino_ratio | -0.6334 |
| max_drawdown | 0.5396 |
| cagr | -0.2506 |
| net_avg_win | 55.7238 |
| net_avg_loss | -84.6938 |
| avg_hold_time_bars | 5.4653 |
| exposure | 0.0715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
