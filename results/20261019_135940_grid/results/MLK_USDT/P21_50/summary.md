# EMA Hourly Continuation — MLK/USDT P21_50

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1283 |
| net_profit_factor | 0.2408 |
| net_win_rate | 0.2673 |
| gross_profit_factor | 0.5662 |
| gross_win_rate | 0.2853 |
| sharpe_ratio | -16.6856 |
| sortino_ratio | -8.6866 |
| max_drawdown | 1.0000 |
| cagr | -0.9884 |
| net_avg_win | 9.2483 |
| net_avg_loss | -14.0128 |
| avg_hold_time_bars | 3.8737 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
