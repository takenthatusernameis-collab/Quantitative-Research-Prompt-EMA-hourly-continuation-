# EMA Hourly Continuation — SAFE/USDT P20_34

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1099 |
| net_profit_factor | 0.3406 |
| net_win_rate | 0.4322 |
| gross_profit_factor | 0.7477 |
| gross_win_rate | 0.4550 |
| sharpe_ratio | -9.2613 |
| sortino_ratio | -4.3670 |
| max_drawdown | 0.9955 |
| cagr | -0.8839 |
| net_avg_win | 10.8232 |
| net_avg_loss | -24.1897 |
| avg_hold_time_bars | 3.2238 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
