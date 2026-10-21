# EMA Hourly Continuation — LDO/USDT P55_100

**Symbol:** LDO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9466 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.8402 |
| sortino_ratio | -0.5099 |
| max_drawdown | 0.4742 |
| cagr | -0.2089 |
| net_avg_win | 68.4992 |
| net_avg_loss | -88.8169 |
| avg_hold_time_bars | 7.4574 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
