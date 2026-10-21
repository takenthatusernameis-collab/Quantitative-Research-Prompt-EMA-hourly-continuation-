# EMA Hourly Continuation — PYTH/USDT P20_21

**Symbol:** PYTH/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 125 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.5120 |
| gross_profit_factor | 1.0478 |
| gross_win_rate | 0.5120 |
| sharpe_ratio | -0.8722 |
| sortino_ratio | -0.1403 |
| max_drawdown | 0.1910 |
| cagr | -0.0626 |
| net_avg_win | 82.3731 |
| net_avg_loss | -110.9735 |
| avg_hold_time_bars | 4.1200 |
| exposure | 0.0234 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
