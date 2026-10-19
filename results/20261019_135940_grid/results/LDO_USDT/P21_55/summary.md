# EMA Hourly Continuation — LDO/USDT P21_55

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.4701 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -7.5537 |
| sortino_ratio | -3.3810 |
| max_drawdown | 0.9847 |
| cagr | -0.8106 |
| net_avg_win | 19.6316 |
| net_avg_loss | -32.4876 |
| avg_hold_time_bars | 4.6971 |
| exposure | 0.2171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
