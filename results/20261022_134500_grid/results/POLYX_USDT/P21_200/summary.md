# EMA Hourly Continuation — POLYX/USDT P21_200

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.5130 |
| gross_profit_factor | 1.0871 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -1.4871 |
| sortino_ratio | -0.4139 |
| max_drawdown | 0.4300 |
| cagr | -0.1773 |
| net_avg_win | 66.3139 |
| net_avg_loss | -90.4523 |
| avg_hold_time_bars | 35.1010 |
| exposure | 0.6159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
