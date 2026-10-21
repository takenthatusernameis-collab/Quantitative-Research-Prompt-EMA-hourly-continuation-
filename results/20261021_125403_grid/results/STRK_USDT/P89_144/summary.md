# EMA Hourly Continuation — STRK/USDT P89_144

**Symbol:** STRK/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.8936 |
| net_win_rate | 0.5294 |
| gross_profit_factor | 1.1300 |
| gross_win_rate | 0.5294 |
| sharpe_ratio | -0.5874 |
| sortino_ratio | -0.1354 |
| max_drawdown | 0.2820 |
| cagr | -0.0624 |
| net_avg_win | 92.9855 |
| net_avg_loss | -117.0672 |
| avg_hold_time_bars | 8.0235 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
