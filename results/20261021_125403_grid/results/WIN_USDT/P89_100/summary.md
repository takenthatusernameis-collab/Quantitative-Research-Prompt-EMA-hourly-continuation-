# EMA Hourly Continuation — WIN/USDT P89_100

**Symbol:** WIN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 87 |
| net_profit_factor | 0.4402 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.6993 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -2.2889 |
| sortino_ratio | -0.3074 |
| max_drawdown | 0.3154 |
| cagr | -0.1329 |
| net_avg_win | 65.7767 |
| net_avg_loss | -105.4664 |
| avg_hold_time_bars | 6.8276 |
| exposure | 0.0270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
