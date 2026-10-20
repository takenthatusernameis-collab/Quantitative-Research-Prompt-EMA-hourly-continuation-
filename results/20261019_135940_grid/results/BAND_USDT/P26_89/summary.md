# EMA Hourly Continuation — BAND/USDT P26_89

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.6031 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.9406 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -4.4332 |
| sortino_ratio | -1.5998 |
| max_drawdown | 0.8571 |
| cagr | -0.5292 |
| net_avg_win | 42.3769 |
| net_avg_loss | -61.5800 |
| avg_hold_time_bars | 10.7856 |
| exposure | 0.3187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
