# EMA Hourly Continuation — AMP/USDT P26_144

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.5691 |
| net_win_rate | 0.4295 |
| gross_profit_factor | 0.7258 |
| gross_win_rate | 0.4295 |
| sharpe_ratio | -3.5748 |
| sortino_ratio | -1.0945 |
| max_drawdown | 0.7525 |
| cagr | -0.3975 |
| net_avg_win | 47.2976 |
| net_avg_loss | -62.5667 |
| avg_hold_time_bars | 21.0406 |
| exposure | 0.4476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
