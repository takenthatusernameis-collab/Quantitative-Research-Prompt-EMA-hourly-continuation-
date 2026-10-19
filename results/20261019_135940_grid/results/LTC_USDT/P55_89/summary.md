# EMA Hourly Continuation — LTC/USDT P55_89

**Symbol:** LTC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.2525 |
| net_win_rate | 0.3781 |
| gross_profit_factor | 0.6984 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -9.7171 |
| sortino_ratio | -3.7562 |
| max_drawdown | 0.9921 |
| cagr | -0.8532 |
| net_avg_win | 12.2714 |
| net_avg_loss | -29.5531 |
| avg_hold_time_bars | 3.8670 |
| exposure | 0.1269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
