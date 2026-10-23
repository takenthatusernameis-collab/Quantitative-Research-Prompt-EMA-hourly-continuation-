# EMA Hourly Continuation — W/USDT P26_200

**Symbol:** W/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.9203 |
| net_win_rate | 0.5414 |
| gross_profit_factor | 1.1883 |
| gross_win_rate | 0.5442 |
| sharpe_ratio | -0.4300 |
| sortino_ratio | -0.1171 |
| max_drawdown | 0.2868 |
| cagr | -0.0581 |
| net_avg_win | 82.2370 |
| net_avg_loss | -105.5035 |
| avg_hold_time_bars | 36.4282 |
| exposure | 0.5994 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
