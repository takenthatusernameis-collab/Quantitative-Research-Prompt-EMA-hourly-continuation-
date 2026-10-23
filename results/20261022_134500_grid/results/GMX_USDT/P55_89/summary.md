# EMA Hourly Continuation — GMX/USDT P55_89

**Symbol:** GMX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.4760 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8835 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -6.2220 |
| sortino_ratio | -2.3302 |
| max_drawdown | 0.9401 |
| cagr | -0.6711 |
| net_avg_win | 27.3265 |
| net_avg_loss | -47.2648 |
| avg_hold_time_bars | 4.7424 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
