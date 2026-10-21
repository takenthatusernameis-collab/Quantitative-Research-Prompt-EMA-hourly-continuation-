# EMA Hourly Continuation — XLM/USDT P144_200

**Symbol:** XLM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.5174 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7786 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -2.5813 |
| sortino_ratio | -0.4777 |
| max_drawdown | 0.4336 |
| cagr | -0.1971 |
| net_avg_win | 62.2454 |
| net_avg_loss | -93.4241 |
| avg_hold_time_bars | 7.0778 |
| exposure | 0.0537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
