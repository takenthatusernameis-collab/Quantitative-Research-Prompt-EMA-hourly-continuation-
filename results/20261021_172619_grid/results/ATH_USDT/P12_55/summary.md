# EMA Hourly Continuation — ATH/USDT P12_55

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.8785 |
| net_win_rate | 0.5239 |
| gross_profit_factor | 1.0913 |
| gross_win_rate | 0.5239 |
| sharpe_ratio | -0.9172 |
| sortino_ratio | -0.3242 |
| max_drawdown | 0.3531 |
| cagr | -0.1430 |
| net_avg_win | 74.4284 |
| net_avg_loss | -93.2270 |
| avg_hold_time_bars | 11.9841 |
| exposure | 0.3282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
