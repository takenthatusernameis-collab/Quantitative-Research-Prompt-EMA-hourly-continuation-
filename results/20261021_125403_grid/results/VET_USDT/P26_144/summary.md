# EMA Hourly Continuation — VET/USDT P26_144

**Symbol:** VET/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 403 |
| net_profit_factor | 0.8333 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -1.0893 |
| sortino_ratio | -0.3139 |
| max_drawdown | 0.3395 |
| cagr | -0.1364 |
| net_avg_win | 74.0325 |
| net_avg_loss | -94.7657 |
| avg_hold_time_bars | 24.0596 |
| exposure | 0.4407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
