# EMA Hourly Continuation — WEMIX/USDT P50_144

**Symbol:** WEMIX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 822 |
| net_profit_factor | 0.3292 |
| net_win_rate | 0.3054 |
| gross_profit_factor | 0.5370 |
| gross_win_rate | 0.3175 |
| sharpe_ratio | -11.4681 |
| sortino_ratio | -4.6732 |
| max_drawdown | 0.9977 |
| cagr | -0.9110 |
| net_avg_win | 19.5093 |
| net_avg_loss | -26.0488 |
| avg_hold_time_bars | 8.8200 |
| exposure | 0.3295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
