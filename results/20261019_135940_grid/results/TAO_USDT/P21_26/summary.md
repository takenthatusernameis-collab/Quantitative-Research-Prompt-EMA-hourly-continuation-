# EMA Hourly Continuation — TAO/USDT P21_26

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.2780 |
| net_win_rate | 0.3364 |
| gross_profit_factor | 0.6783 |
| gross_win_rate | 0.3719 |
| sharpe_ratio | -14.8751 |
| sortino_ratio | -7.4417 |
| max_drawdown | 1.0000 |
| cagr | -0.9817 |
| net_avg_win | 9.6724 |
| net_avg_loss | -17.6423 |
| avg_hold_time_bars | 1.7194 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
