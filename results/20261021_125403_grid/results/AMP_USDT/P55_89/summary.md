# EMA Hourly Continuation — AMP/USDT P55_89

**Symbol:** AMP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.6498 |
| net_win_rate | 0.4827 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4827 |
| sharpe_ratio | -2.6052 |
| sortino_ratio | -0.6940 |
| max_drawdown | 0.5714 |
| cagr | -0.2724 |
| net_avg_win | 61.0987 |
| net_avg_loss | -87.7288 |
| avg_hold_time_bars | 7.3642 |
| exposure | 0.1158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
