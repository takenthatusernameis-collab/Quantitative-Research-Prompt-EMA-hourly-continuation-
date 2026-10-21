# EMA Hourly Continuation — T/USDT P50_144

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.7198 |
| net_win_rate | 0.5042 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -1.8535 |
| sortino_ratio | -0.5016 |
| max_drawdown | 0.4475 |
| cagr | -0.2059 |
| net_avg_win | 62.5891 |
| net_avg_loss | -88.4216 |
| avg_hold_time_bars | 17.2340 |
| exposure | 0.2800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
