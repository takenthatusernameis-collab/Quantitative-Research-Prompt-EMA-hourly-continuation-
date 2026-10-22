# EMA Hourly Continuation — DODO/USDT P21_34

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.5730 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8174 |
| gross_win_rate | 0.4515 |
| sharpe_ratio | -3.5423 |
| sortino_ratio | -1.0251 |
| max_drawdown | 0.6944 |
| cagr | -0.3749 |
| net_avg_win | 50.0848 |
| net_avg_loss | -71.9402 |
| avg_hold_time_bars | 6.1990 |
| exposure | 0.1156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
