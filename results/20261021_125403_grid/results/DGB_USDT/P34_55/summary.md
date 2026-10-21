# EMA Hourly Continuation — DGB/USDT P34_55

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.6405 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.8810 |
| gross_win_rate | 0.4674 |
| sharpe_ratio | -2.3897 |
| sortino_ratio | -0.5825 |
| max_drawdown | 0.5146 |
| cagr | -0.2342 |
| net_avg_win | 63.9733 |
| net_avg_loss | -87.6385 |
| avg_hold_time_bars | 6.7491 |
| exposure | 0.0893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
