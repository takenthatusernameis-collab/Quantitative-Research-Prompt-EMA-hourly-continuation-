# EMA Hourly Continuation — ATH/USDT P34_144

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.9606 |
| net_win_rate | 0.5385 |
| gross_profit_factor | 1.1499 |
| gross_win_rate | 0.5385 |
| sharpe_ratio | -0.1814 |
| sortino_ratio | -0.0498 |
| max_drawdown | 0.1206 |
| cagr | -0.0284 |
| net_avg_win | 87.8273 |
| net_avg_loss | -106.6704 |
| avg_hold_time_bars | 23.3462 |
| exposure | 0.3825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
