# EMA Hourly Continuation — NOT/USDT P8_200

**Symbol:** NOT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.9592 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.1088 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -0.1284 |
| sortino_ratio | -0.0235 |
| max_drawdown | 0.0929 |
| cagr | -0.0134 |
| net_avg_win | 92.1936 |
| net_avg_loss | -106.5102 |
| avg_hold_time_bars | 120.3782 |
| exposure | 0.8821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
