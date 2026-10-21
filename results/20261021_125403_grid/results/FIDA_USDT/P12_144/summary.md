# EMA Hourly Continuation — FIDA/USDT P12_144

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9277 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -1.7749 |
| sortino_ratio | -0.5052 |
| max_drawdown | 0.4540 |
| cagr | -0.2083 |
| net_avg_win | 67.9448 |
| net_avg_loss | -85.1876 |
| avg_hold_time_bars | 37.0050 |
| exposure | 0.6715 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
