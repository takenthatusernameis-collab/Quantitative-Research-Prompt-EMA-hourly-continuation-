# EMA Hourly Continuation — OP/USDT P12_89

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.5956 |
| net_win_rate | 0.4512 |
| gross_profit_factor | 0.8766 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -4.5261 |
| sortino_ratio | -1.6540 |
| max_drawdown | 0.8706 |
| cagr | -0.5456 |
| net_avg_win | 41.6259 |
| net_avg_loss | -57.4569 |
| avg_hold_time_bars | 17.9852 |
| exposure | 0.5526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
