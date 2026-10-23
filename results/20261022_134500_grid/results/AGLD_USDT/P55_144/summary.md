# EMA Hourly Continuation — AGLD/USDT P55_144

**Symbol:** AGLD/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7049 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 1.0166 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -2.8388 |
| sortino_ratio | -0.9206 |
| max_drawdown | 0.6844 |
| cagr | -0.3479 |
| net_avg_win | 61.8122 |
| net_avg_loss | -82.8188 |
| avg_hold_time_bars | 11.0229 |
| exposure | 0.2619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
