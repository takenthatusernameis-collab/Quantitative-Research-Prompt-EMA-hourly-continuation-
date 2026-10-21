# EMA Hourly Continuation — AURORA/USDT P34_144

**Symbol:** AURORA/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.6925 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9201 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.2147 |
| sortino_ratio | -0.5765 |
| max_drawdown | 0.4976 |
| cagr | -0.2337 |
| net_avg_win | 69.0508 |
| net_avg_loss | -90.5936 |
| avg_hold_time_bars | 24.3144 |
| exposure | 0.3691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
