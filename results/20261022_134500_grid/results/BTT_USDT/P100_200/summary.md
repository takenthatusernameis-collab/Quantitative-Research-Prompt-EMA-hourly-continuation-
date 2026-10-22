# EMA Hourly Continuation — BTT/USDT P100_200

**Symbol:** BTT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.3636 |
| net_win_rate | 0.3903 |
| gross_profit_factor | 0.8523 |
| gross_win_rate | 0.4302 |
| sharpe_ratio | -6.5688 |
| sortino_ratio | -1.7633 |
| max_drawdown | 0.8980 |
| cagr | -0.5969 |
| net_avg_win | 37.4444 |
| net_avg_loss | -65.9300 |
| avg_hold_time_bars | 13.4758 |
| exposure | 0.2150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
