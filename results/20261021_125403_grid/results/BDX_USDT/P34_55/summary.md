# EMA Hourly Continuation — BDX/USDT P34_55

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.3258 |
| net_win_rate | 0.3382 |
| gross_profit_factor | 0.5615 |
| gross_win_rate | 0.3382 |
| sharpe_ratio | -5.0584 |
| sortino_ratio | -1.0514 |
| max_drawdown | 0.7183 |
| cagr | -0.3905 |
| net_avg_win | 49.1254 |
| net_avg_loss | -77.0444 |
| avg_hold_time_bars | 5.4251 |
| exposure | 0.0510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
