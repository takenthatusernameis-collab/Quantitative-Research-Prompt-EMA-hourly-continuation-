# EMA Hourly Continuation — CARV/USDT P21_26

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.7077 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5174 |
| sharpe_ratio | -1.9034 |
| sortino_ratio | -0.4629 |
| max_drawdown | 0.3616 |
| cagr | -0.1899 |
| net_avg_win | 70.7349 |
| net_avg_loss | -107.1569 |
| avg_hold_time_bars | 6.3783 |
| exposure | 0.0826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
