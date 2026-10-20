# EMA Hourly Continuation — RPL/USDT P21_34

**Symbol:** RPL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.3472 |
| net_win_rate | 0.4058 |
| gross_profit_factor | 0.7796 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -9.5908 |
| sortino_ratio | -4.3109 |
| max_drawdown | 0.9955 |
| cagr | -0.8830 |
| net_avg_win | 12.9449 |
| net_avg_loss | -25.4587 |
| avg_hold_time_bars | 3.9663 |
| exposure | 0.1809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
