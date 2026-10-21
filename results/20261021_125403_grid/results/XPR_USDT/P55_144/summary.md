# EMA Hourly Continuation — XPR/USDT P55_144

**Symbol:** XPR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6678 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8711 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.0964 |
| sortino_ratio | -0.5019 |
| max_drawdown | 0.4472 |
| cagr | -0.2053 |
| net_avg_win | 66.7790 |
| net_avg_loss | -87.9927 |
| avg_hold_time_bars | 14.5035 |
| exposure | 0.1859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
