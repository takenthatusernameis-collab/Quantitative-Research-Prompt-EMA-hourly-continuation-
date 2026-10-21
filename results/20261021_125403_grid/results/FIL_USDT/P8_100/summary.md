# EMA Hourly Continuation — FIL/USDT P8_100

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.8005 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.3853 |
| sortino_ratio | -0.3966 |
| max_drawdown | 0.4205 |
| cagr | -0.1684 |
| net_avg_win | 75.1155 |
| net_avg_loss | -91.0797 |
| avg_hold_time_bars | 37.8010 |
| exposure | 0.6907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
