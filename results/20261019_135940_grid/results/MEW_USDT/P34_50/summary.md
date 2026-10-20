# EMA Hourly Continuation — MEW/USDT P34_50

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 891 |
| net_profit_factor | 0.3544 |
| net_win_rate | 0.4265 |
| gross_profit_factor | 0.6462 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -8.4779 |
| sortino_ratio | -3.5727 |
| max_drawdown | 0.9890 |
| cagr | -0.8324 |
| net_avg_win | 14.2853 |
| net_avg_loss | -29.9719 |
| avg_hold_time_bars | 2.6790 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
