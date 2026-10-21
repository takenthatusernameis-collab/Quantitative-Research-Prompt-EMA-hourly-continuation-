# EMA Hourly Continuation — OP/USDT P34_89

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7927 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0117 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5881 |
| sortino_ratio | -0.4640 |
| max_drawdown | 0.4671 |
| cagr | -0.1927 |
| net_avg_win | 76.4454 |
| net_avg_loss | -96.4416 |
| avg_hold_time_bars | 12.1106 |
| exposure | 0.2290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
