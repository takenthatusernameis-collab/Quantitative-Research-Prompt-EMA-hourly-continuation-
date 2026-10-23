# EMA Hourly Continuation — PUNDIX/USDT P12_26

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1330 |
| net_profit_factor | 0.2973 |
| net_win_rate | 0.4083 |
| gross_profit_factor | 0.6975 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -11.5533 |
| sortino_ratio | -6.0066 |
| max_drawdown | 0.9994 |
| cagr | -0.9492 |
| net_avg_win | 7.7872 |
| net_avg_loss | -18.0722 |
| avg_hold_time_bars | 3.9361 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
