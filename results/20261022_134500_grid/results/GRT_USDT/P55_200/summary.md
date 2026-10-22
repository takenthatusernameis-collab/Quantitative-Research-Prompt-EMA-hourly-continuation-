# EMA Hourly Continuation — GRT/USDT P55_200

**Symbol:** GRT/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6797 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9912 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -2.4762 |
| sortino_ratio | -0.6770 |
| max_drawdown | 0.5770 |
| cagr | -0.2770 |
| net_avg_win | 63.0751 |
| net_avg_loss | -91.8214 |
| avg_hold_time_bars | 21.6111 |
| exposure | 0.3697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
