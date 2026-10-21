# EMA Hourly Continuation — ENA/USDT P26_144

**Symbol:** ENA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.9296 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0602 |
| gross_win_rate | 0.5198 |
| sharpe_ratio | -0.3483 |
| sortino_ratio | -0.0942 |
| max_drawdown | 0.2626 |
| cagr | -0.0472 |
| net_avg_win | 82.4662 |
| net_avg_loss | -94.9336 |
| avg_hold_time_bars | 28.3785 |
| exposure | 0.4566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
