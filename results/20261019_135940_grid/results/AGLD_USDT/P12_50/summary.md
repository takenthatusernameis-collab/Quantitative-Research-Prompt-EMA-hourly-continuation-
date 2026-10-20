# EMA Hourly Continuation — AGLD/USDT P12_50

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1041 |
| net_profit_factor | 0.5448 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8884 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -6.2379 |
| sortino_ratio | -2.8172 |
| max_drawdown | 0.9693 |
| cagr | -0.7431 |
| net_avg_win | 24.5811 |
| net_avg_loss | -37.2862 |
| avg_hold_time_bars | 7.8261 |
| exposure | 0.3687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
