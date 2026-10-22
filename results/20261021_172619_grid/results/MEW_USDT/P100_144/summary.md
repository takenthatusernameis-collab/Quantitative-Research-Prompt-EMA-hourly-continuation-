# EMA Hourly Continuation — MEW/USDT P100_144

**Symbol:** MEW/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.7227 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4850 |
| sharpe_ratio | -1.6658 |
| sortino_ratio | -0.3884 |
| max_drawdown | 0.3780 |
| cagr | -0.1634 |
| net_avg_win | 72.9742 |
| net_avg_loss | -95.0761 |
| avg_hold_time_bars | 6.5263 |
| exposure | 0.0789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
