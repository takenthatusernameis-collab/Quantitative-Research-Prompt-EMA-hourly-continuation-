# EMA Hourly Continuation — GMX/USDT P8_144

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.6932 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9652 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.0573 |
| sortino_ratio | -1.0245 |
| max_drawdown | 0.7301 |
| cagr | -0.3819 |
| net_avg_win | 58.8898 |
| net_avg_loss | -77.7341 |
| avg_hold_time_bars | 27.9787 |
| exposure | 0.7160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
