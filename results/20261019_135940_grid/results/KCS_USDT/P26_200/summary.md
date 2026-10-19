# EMA Hourly Continuation — KCS/USDT P26_200

**Symbol:** KCS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.3733 |
| net_win_rate | 0.3842 |
| gross_profit_factor | 0.7936 |
| gross_win_rate | 0.4163 |
| sharpe_ratio | -6.5036 |
| sortino_ratio | -1.8409 |
| max_drawdown | 0.9086 |
| cagr | -0.6143 |
| net_avg_win | 34.6857 |
| net_avg_loss | -57.9871 |
| avg_hold_time_bars | 30.3054 |
| exposure | 0.5593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
