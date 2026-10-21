# EMA Hourly Continuation — FET/USDT P26_55

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7699 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.5737 |
| sortino_ratio | -0.4358 |
| max_drawdown | 0.4473 |
| cagr | -0.1818 |
| net_avg_win | 71.5940 |
| net_avg_loss | -91.0200 |
| avg_hold_time_bars | 7.2353 |
| exposure | 0.1230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
