# EMA Hourly Continuation — LDO/USDT P21_26

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1244 |
| net_profit_factor | 0.2048 |
| net_win_rate | 0.3529 |
| gross_profit_factor | 0.5675 |
| gross_win_rate | 0.4011 |
| sharpe_ratio | -14.7840 |
| sortino_ratio | -7.5794 |
| max_drawdown | 1.0000 |
| cagr | -0.9827 |
| net_avg_win | 5.8657 |
| net_avg_loss | -15.6207 |
| avg_hold_time_bars | 1.7717 |
| exposure | 0.1002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
