# EMA Hourly Continuation — BTT/USDT P34_89

**Symbol:** BTT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.4944 |
| net_win_rate | 0.4225 |
| gross_profit_factor | 0.8109 |
| gross_win_rate | 0.4250 |
| sharpe_ratio | -5.1594 |
| sortino_ratio | -1.4816 |
| max_drawdown | 0.8310 |
| cagr | -0.5039 |
| net_avg_win | 47.9119 |
| net_avg_loss | -70.8975 |
| avg_hold_time_bars | 14.3600 |
| exposure | 0.2611 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
