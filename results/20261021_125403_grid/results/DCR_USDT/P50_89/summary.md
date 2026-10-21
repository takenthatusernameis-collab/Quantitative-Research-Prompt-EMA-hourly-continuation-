# EMA Hourly Continuation — DCR/USDT P50_89

**Symbol:** DCR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4532 |
| gross_profit_factor | 0.8291 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -3.4212 |
| sortino_ratio | -0.9818 |
| max_drawdown | 0.6792 |
| cagr | -0.3628 |
| net_avg_win | 49.7083 |
| net_avg_loss | -71.7951 |
| avg_hold_time_bars | 7.9975 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
