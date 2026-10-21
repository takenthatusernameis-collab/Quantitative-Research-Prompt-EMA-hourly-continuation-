# EMA Hourly Continuation — MLK/USDT P55_144

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.4035 |
| net_win_rate | 0.3371 |
| gross_profit_factor | 0.5487 |
| gross_win_rate | 0.3428 |
| sharpe_ratio | -5.4097 |
| sortino_ratio | -1.4319 |
| max_drawdown | 0.8160 |
| cagr | -0.4889 |
| net_avg_win | 46.3893 |
| net_avg_loss | -58.4642 |
| avg_hold_time_bars | 13.3569 |
| exposure | 0.2134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
