# EMA Hourly Continuation — QNT/USDT P34_144

**Symbol:** QNT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.5311 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.8635 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -4.3405 |
| sortino_ratio | -1.5571 |
| max_drawdown | 0.8508 |
| cagr | -0.5226 |
| net_avg_win | 31.3333 |
| net_avg_loss | -52.9254 |
| avg_hold_time_bars | 12.0899 |
| exposure | 0.3545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
