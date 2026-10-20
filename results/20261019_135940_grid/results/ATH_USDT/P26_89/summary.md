# EMA Hourly Continuation — ATH/USDT P26_89

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6232 |
| net_win_rate | 0.4930 |
| gross_profit_factor | 0.9478 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.7977 |
| sortino_ratio | -1.4818 |
| max_drawdown | 0.8172 |
| cagr | -0.5060 |
| net_avg_win | 37.9596 |
| net_avg_loss | -59.2287 |
| avg_hold_time_bars | 7.9567 |
| exposure | 0.2761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
