# EMA Hourly Continuation — XTZ/USDT P12_144

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.6713 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 1.0286 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -2.3805 |
| sortino_ratio | -0.6870 |
| max_drawdown | 0.5769 |
| cagr | -0.2795 |
| net_avg_win | 55.6201 |
| net_avg_loss | -80.1264 |
| avg_hold_time_bars | 38.0549 |
| exposure | 0.7248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
