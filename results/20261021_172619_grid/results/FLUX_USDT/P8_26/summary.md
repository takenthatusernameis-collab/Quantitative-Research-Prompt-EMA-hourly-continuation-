# EMA Hourly Continuation — FLUX/USDT P8_26

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.8000 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -1.8205 |
| sortino_ratio | -0.6724 |
| max_drawdown | 0.6119 |
| cagr | -0.2668 |
| net_avg_win | 63.8934 |
| net_avg_loss | -84.6048 |
| avg_hold_time_bars | 6.2898 |
| exposure | 0.1884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
