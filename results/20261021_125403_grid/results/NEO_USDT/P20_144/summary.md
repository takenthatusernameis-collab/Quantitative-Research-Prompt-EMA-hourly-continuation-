# EMA Hourly Continuation — NEO/USDT P20_144

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.7975 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 0.9985 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.1843 |
| sortino_ratio | -0.3107 |
| max_drawdown | 0.3717 |
| cagr | -0.1341 |
| net_avg_win | 70.6719 |
| net_avg_loss | -90.2227 |
| avg_hold_time_bars | 38.5612 |
| exposure | 0.5872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
