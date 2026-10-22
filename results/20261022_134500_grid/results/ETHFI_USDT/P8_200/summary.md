# EMA Hourly Continuation — ETHFI/USDT P8_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.7985 |
| net_win_rate | 0.4898 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.4386 |
| sortino_ratio | -0.3771 |
| max_drawdown | 0.4226 |
| cagr | -0.1630 |
| net_avg_win | 84.9924 |
| net_avg_loss | -102.1853 |
| avg_hold_time_bars | 51.8163 |
| exposure | 0.8079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
