# EMA Hourly Continuation — MOG/USDT P20_144

**Symbol:** MOG/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.8265 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9454 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -1.1241 |
| sortino_ratio | -0.2972 |
| max_drawdown | 0.3734 |
| cagr | -0.1297 |
| net_avg_win | 84.4355 |
| net_avg_loss | -97.7236 |
| avg_hold_time_bars | 34.9810 |
| exposure | 0.5478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
