# EMA Hourly Continuation — KAS/USDT P34_144

**Symbol:** KAS/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8029 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 0.9969 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.2008 |
| sortino_ratio | -0.3231 |
| max_drawdown | 0.3276 |
| cagr | -0.1392 |
| net_avg_win | 71.7760 |
| net_avg_loss | -90.9288 |
| avg_hold_time_bars | 19.8612 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
