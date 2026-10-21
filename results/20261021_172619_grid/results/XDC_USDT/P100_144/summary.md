# EMA Hourly Continuation — XDC/USDT P100_144

**Symbol:** XDC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 203 |
| net_profit_factor | 0.5334 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.8469 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.5714 |
| sortino_ratio | -0.5258 |
| max_drawdown | 0.4613 |
| cagr | -0.2155 |
| net_avg_win | 54.9118 |
| net_avg_loss | -90.5574 |
| avg_hold_time_bars | 6.3300 |
| exposure | 0.0584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
