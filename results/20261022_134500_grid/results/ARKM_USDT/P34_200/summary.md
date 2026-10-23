# EMA Hourly Continuation — ARKM/USDT P34_200

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.6726 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -2.4188 |
| sortino_ratio | -0.6922 |
| max_drawdown | 0.5697 |
| cagr | -0.2798 |
| net_avg_win | 59.4376 |
| net_avg_loss | -77.9304 |
| avg_hold_time_bars | 25.9469 |
| exposure | 0.4883 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
