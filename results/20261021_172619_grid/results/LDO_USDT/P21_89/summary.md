# EMA Hourly Continuation — LDO/USDT P21_89

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6887 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8304 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -2.7072 |
| sortino_ratio | -0.8422 |
| max_drawdown | 0.6419 |
| cagr | -0.3215 |
| net_avg_win | 63.4648 |
| net_avg_loss | -75.4560 |
| avg_hold_time_bars | 16.2303 |
| exposure | 0.3556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
