# EMA Hourly Continuation — ZEN/USDT P12_144

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8987 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0610 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -0.5925 |
| sortino_ratio | -0.1599 |
| max_drawdown | 0.2285 |
| cagr | -0.0746 |
| net_avg_win | 86.2106 |
| net_avg_loss | -102.0972 |
| avg_hold_time_bars | 42.9122 |
| exposure | 0.6885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
