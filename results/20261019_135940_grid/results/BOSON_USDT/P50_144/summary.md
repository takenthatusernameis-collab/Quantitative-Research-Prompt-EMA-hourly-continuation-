# EMA Hourly Continuation — BOSON/USDT P50_144

**Symbol:** BOSON/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.7227 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9686 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.5299 |
| sortino_ratio | -0.8218 |
| max_drawdown | 0.6207 |
| cagr | -0.3180 |
| net_avg_win | 63.8828 |
| net_avg_loss | -81.5901 |
| avg_hold_time_bars | 11.6248 |
| exposure | 0.2774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
