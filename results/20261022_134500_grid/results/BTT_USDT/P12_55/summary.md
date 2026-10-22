# EMA Hourly Continuation — BTT/USDT P12_55

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 982 |
| net_profit_factor | 0.3578 |
| net_win_rate | 0.3615 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4196 |
| sharpe_ratio | -12.1048 |
| sortino_ratio | -5.4586 |
| max_drawdown | 0.9993 |
| cagr | -0.9439 |
| net_avg_win | 15.6838 |
| net_avg_loss | -24.8175 |
| avg_hold_time_bars | 9.7648 |
| exposure | 0.4359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
