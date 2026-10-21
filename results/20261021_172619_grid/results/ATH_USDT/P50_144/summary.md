# EMA Hourly Continuation — ATH/USDT P50_144

**Symbol:** ATH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.7771 |
| net_win_rate | 0.4873 |
| gross_profit_factor | 0.9392 |
| gross_win_rate | 0.4873 |
| sharpe_ratio | -1.4233 |
| sortino_ratio | -0.3725 |
| max_drawdown | 0.3519 |
| cagr | -0.1584 |
| net_avg_win | 75.5723 |
| net_avg_loss | -92.4457 |
| avg_hold_time_bars | 17.0443 |
| exposure | 0.2611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
