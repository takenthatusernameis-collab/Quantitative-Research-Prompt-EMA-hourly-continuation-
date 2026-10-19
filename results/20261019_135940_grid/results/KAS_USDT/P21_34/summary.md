# EMA Hourly Continuation — KAS/USDT P21_34

**Symbol:** KAS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1148 |
| net_profit_factor | 0.2923 |
| net_win_rate | 0.4294 |
| gross_profit_factor | 0.8035 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -10.6243 |
| sortino_ratio | -5.1090 |
| max_drawdown | 0.9987 |
| cagr | -0.9284 |
| net_avg_win | 8.3673 |
| net_avg_loss | -21.5447 |
| avg_hold_time_bars | 2.4094 |
| exposure | 0.1257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
