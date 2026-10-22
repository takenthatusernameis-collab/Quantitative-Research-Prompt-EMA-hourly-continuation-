# EMA Hourly Continuation — WOO/USDT P55_144

**Symbol:** WOO/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.6895 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8597 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -2.2784 |
| sortino_ratio | -0.6113 |
| max_drawdown | 0.5203 |
| cagr | -0.2454 |
| net_avg_win | 68.2330 |
| net_avg_loss | -85.0422 |
| avg_hold_time_bars | 13.9272 |
| exposure | 0.2260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
