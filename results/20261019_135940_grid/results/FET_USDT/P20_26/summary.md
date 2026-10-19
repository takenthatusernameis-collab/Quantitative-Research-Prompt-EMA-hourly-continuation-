# EMA Hourly Continuation — FET/USDT P20_26

**Symbol:** FET/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.3289 |
| net_win_rate | 0.3764 |
| gross_profit_factor | 0.8057 |
| gross_win_rate | 0.4098 |
| sharpe_ratio | -13.4230 |
| sortino_ratio | -6.7777 |
| max_drawdown | 0.9999 |
| cagr | -0.9715 |
| net_avg_win | 10.5817 |
| net_avg_loss | -19.4237 |
| avg_hold_time_bars | 1.7496 |
| exposure | 0.0978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
