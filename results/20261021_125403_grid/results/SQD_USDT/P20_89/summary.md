# EMA Hourly Continuation — SQD/USDT P20_89

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.9220 |
| net_win_rate | 0.5236 |
| gross_profit_factor | 1.0933 |
| gross_win_rate | 0.5236 |
| sharpe_ratio | -0.5533 |
| sortino_ratio | -0.1827 |
| max_drawdown | 0.3193 |
| cagr | -0.0865 |
| net_avg_win | 87.7312 |
| net_avg_loss | -104.5858 |
| avg_hold_time_bars | 14.1161 |
| exposure | 0.3371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
