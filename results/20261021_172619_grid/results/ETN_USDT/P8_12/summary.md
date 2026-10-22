# EMA Hourly Continuation — ETN/USDT P8_12

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 246 |
| net_profit_factor | 0.3035 |
| net_win_rate | 0.3171 |
| gross_profit_factor | 0.4041 |
| gross_win_rate | 0.3171 |
| sharpe_ratio | -5.4353 |
| sortino_ratio | -1.3159 |
| max_drawdown | 0.7307 |
| cagr | -0.4614 |
| net_avg_win | 40.6493 |
| net_avg_loss | -62.1813 |
| avg_hold_time_bars | 5.0772 |
| exposure | 0.0678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
