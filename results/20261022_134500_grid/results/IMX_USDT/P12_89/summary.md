# EMA Hourly Continuation — IMX/USDT P12_89

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.6559 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4959 |
| sharpe_ratio | -3.2736 |
| sortino_ratio | -1.2454 |
| max_drawdown | 0.7871 |
| cagr | -0.4474 |
| net_avg_win | 41.4355 |
| net_avg_loss | -60.1397 |
| avg_hold_time_bars | 15.5314 |
| exposure | 0.5145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
