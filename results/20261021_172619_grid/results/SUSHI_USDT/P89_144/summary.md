# EMA Hourly Continuation — SUSHI/USDT P89_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.6709 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -1.9253 |
| sortino_ratio | -0.4469 |
| max_drawdown | 0.4034 |
| cagr | -0.1851 |
| net_avg_win | 64.7196 |
| net_avg_loss | -88.7818 |
| avg_hold_time_bars | 7.6264 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
