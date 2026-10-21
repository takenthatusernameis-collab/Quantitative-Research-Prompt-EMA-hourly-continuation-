# EMA Hourly Continuation — ICP/USDT P21_144

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.9197 |
| net_win_rate | 0.5276 |
| gross_profit_factor | 1.1020 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -0.4262 |
| sortino_ratio | -0.1108 |
| max_drawdown | 0.2311 |
| cagr | -0.0535 |
| net_avg_win | 85.9524 |
| net_avg_loss | -104.3807 |
| avg_hold_time_bars | 39.4693 |
| exposure | 0.5849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
