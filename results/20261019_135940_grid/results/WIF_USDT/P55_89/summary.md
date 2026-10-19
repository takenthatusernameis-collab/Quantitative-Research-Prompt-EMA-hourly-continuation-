# EMA Hourly Continuation — WIF/USDT P55_89

**Symbol:** WIF/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.5395 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -5.0192 |
| sortino_ratio | -1.8177 |
| max_drawdown | 0.8923 |
| cagr | -0.5853 |
| net_avg_win | 33.7635 |
| net_avg_loss | -54.9335 |
| avg_hold_time_bars | 4.0076 |
| exposure | 0.1204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
