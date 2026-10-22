# EMA Hourly Continuation — ZEC/USDT P20_50

**Symbol:** ZEC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 932 |
| net_profit_factor | 0.4610 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -6.7856 |
| sortino_ratio | -2.9022 |
| max_drawdown | 0.9737 |
| cagr | -0.7641 |
| net_avg_win | 19.7730 |
| net_avg_loss | -35.3394 |
| avg_hold_time_bars | 4.8219 |
| exposure | 0.2043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
