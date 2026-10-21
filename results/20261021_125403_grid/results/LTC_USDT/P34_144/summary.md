# EMA Hourly Continuation — LTC/USDT P34_144

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6010 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.8093 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -2.9064 |
| sortino_ratio | -0.7759 |
| max_drawdown | 0.6167 |
| cagr | -0.3009 |
| net_avg_win | 56.1861 |
| net_avg_loss | -77.0157 |
| avg_hold_time_bars | 22.8466 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
