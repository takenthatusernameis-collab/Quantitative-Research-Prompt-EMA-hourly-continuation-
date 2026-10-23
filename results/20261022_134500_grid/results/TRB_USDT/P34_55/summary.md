# EMA Hourly Continuation — TRB/USDT P34_55

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.3934 |
| net_win_rate | 0.3978 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4201 |
| sharpe_ratio | -10.4852 |
| sortino_ratio | -4.7110 |
| max_drawdown | 0.9974 |
| cagr | -0.9029 |
| net_avg_win | 16.5409 |
| net_avg_loss | -27.7696 |
| avg_hold_time_bars | 2.8444 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
