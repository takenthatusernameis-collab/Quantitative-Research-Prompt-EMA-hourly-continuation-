# EMA Hourly Continuation — IOTX/USDT P21_200

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.4957 |
| gross_profit_factor | 0.9663 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.2767 |
| sortino_ratio | -0.6922 |
| max_drawdown | 0.5748 |
| cagr | -0.2806 |
| net_avg_win | 54.5919 |
| net_avg_loss | -77.6048 |
| avg_hold_time_bars | 27.0300 |
| exposure | 0.5725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
