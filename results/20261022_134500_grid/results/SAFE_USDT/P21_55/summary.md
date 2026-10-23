# EMA Hourly Continuation — SAFE/USDT P21_55

**Symbol:** SAFE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 910 |
| net_profit_factor | 0.5539 |
| net_win_rate | 0.4725 |
| gross_profit_factor | 0.9576 |
| gross_win_rate | 0.4846 |
| sharpe_ratio | -5.6068 |
| sortino_ratio | -2.3907 |
| max_drawdown | 0.9442 |
| cagr | -0.6821 |
| net_avg_win | 27.2189 |
| net_avg_loss | -44.0198 |
| avg_hold_time_bars | 5.9187 |
| exposure | 0.2467 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
