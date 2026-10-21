# EMA Hourly Continuation — 1INCH/USDT P8_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.7777 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9371 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -1.2815 |
| sortino_ratio | -0.2872 |
| max_drawdown | 0.3104 |
| cagr | -0.1250 |
| net_avg_win | 83.0564 |
| net_avg_loss | -100.1237 |
| avg_hold_time_bars | 73.1694 |
| exposure | 0.8248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
