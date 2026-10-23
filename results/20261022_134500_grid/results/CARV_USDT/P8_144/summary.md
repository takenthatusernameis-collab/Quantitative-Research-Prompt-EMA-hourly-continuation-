# EMA Hourly Continuation — CARV/USDT P8_144

**Symbol:** CARV/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.7039 |
| net_win_rate | 0.4911 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.6312 |
| sortino_ratio | -0.8805 |
| max_drawdown | 0.5898 |
| cagr | -0.3363 |
| net_avg_win | 60.7286 |
| net_avg_loss | -83.2636 |
| avg_hold_time_bars | 27.5867 |
| exposure | 0.6986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
