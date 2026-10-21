# EMA Hourly Continuation — RENDER/USDT P12_26

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7315 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9744 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -2.2010 |
| sortino_ratio | -0.6675 |
| max_drawdown | 0.5087 |
| cagr | -0.2631 |
| net_avg_win | 69.6845 |
| net_avg_loss | -91.3907 |
| avg_hold_time_bars | 5.2513 |
| exposure | 0.1070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
