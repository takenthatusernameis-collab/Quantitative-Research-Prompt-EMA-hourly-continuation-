# EMA Hourly Continuation — FLR/USDT P21_200

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -1.3485 |
| sortino_ratio | -0.3832 |
| max_drawdown | 0.3762 |
| cagr | -0.1626 |
| net_avg_win | 71.1699 |
| net_avg_loss | -90.2415 |
| avg_hold_time_bars | 31.2716 |
| exposure | 0.5600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
