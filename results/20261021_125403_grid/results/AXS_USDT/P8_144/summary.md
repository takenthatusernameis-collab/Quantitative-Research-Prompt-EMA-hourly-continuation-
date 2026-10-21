# EMA Hourly Continuation — AXS/USDT P8_144

**Symbol:** AXS/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.9303 |
| net_win_rate | 0.5311 |
| gross_profit_factor | 1.1148 |
| gross_win_rate | 0.5311 |
| sharpe_ratio | -0.3627 |
| sortino_ratio | -0.0980 |
| max_drawdown | 0.1890 |
| cagr | -0.0488 |
| net_avg_win | 84.1577 |
| net_avg_loss | -102.4542 |
| avg_hold_time_bars | 46.7768 |
| exposure | 0.7493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
