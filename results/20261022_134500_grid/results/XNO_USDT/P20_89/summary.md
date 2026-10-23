# EMA Hourly Continuation — XNO/USDT P20_89

**Symbol:** XNO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.5129 |
| net_win_rate | 0.4040 |
| gross_profit_factor | 0.8020 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -7.5303 |
| sortino_ratio | -3.1802 |
| max_drawdown | 0.9792 |
| cagr | -0.7831 |
| net_avg_win | 28.4608 |
| net_avg_loss | -37.6171 |
| avg_hold_time_bars | 9.1350 |
| exposure | 0.3720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
