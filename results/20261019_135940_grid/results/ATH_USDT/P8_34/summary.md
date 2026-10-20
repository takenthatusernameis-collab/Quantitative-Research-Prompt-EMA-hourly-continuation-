# EMA Hourly Continuation — ATH/USDT P8_34

**Symbol:** ATH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.5470 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9088 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -6.9160 |
| sortino_ratio | -3.6575 |
| max_drawdown | 0.9860 |
| cagr | -0.8327 |
| net_avg_win | 18.7903 |
| net_avg_loss | -31.0657 |
| avg_hold_time_bars | 4.8200 |
| exposure | 0.3114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
