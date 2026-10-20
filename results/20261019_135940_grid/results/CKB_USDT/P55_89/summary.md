# EMA Hourly Continuation — CKB/USDT P55_89

**Symbol:** CKB/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.4947 |
| net_win_rate | 0.4353 |
| gross_profit_factor | 0.8920 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -6.7881 |
| sortino_ratio | -2.5000 |
| max_drawdown | 0.9561 |
| cagr | -0.7093 |
| net_avg_win | 31.5923 |
| net_avg_loss | -49.2243 |
| avg_hold_time_bars | 4.0750 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
