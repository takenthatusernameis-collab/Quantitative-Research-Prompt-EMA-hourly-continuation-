# EMA Hourly Continuation — WIF/USDT P12_55

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.7135 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 1.0488 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -5.0379 |
| sortino_ratio | -2.2772 |
| max_drawdown | 0.9458 |
| cagr | -0.6711 |
| net_avg_win | 46.3846 |
| net_avg_loss | -60.4521 |
| avg_hold_time_bars | 7.5813 |
| exposure | 0.3605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
