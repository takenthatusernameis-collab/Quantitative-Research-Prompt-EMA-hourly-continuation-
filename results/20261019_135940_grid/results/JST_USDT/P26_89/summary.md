# EMA Hourly Continuation — JST/USDT P26_89

**Symbol:** JST/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.3352 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.9181 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -6.9049 |
| sortino_ratio | -2.4653 |
| max_drawdown | 0.9619 |
| cagr | -0.7223 |
| net_avg_win | 16.6437 |
| net_avg_loss | -39.8028 |
| avg_hold_time_bars | 10.1697 |
| exposure | 0.3010 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
