# EMA Hourly Continuation — AGLD/USDT P20_26

**Symbol:** AGLD/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1175 |
| net_profit_factor | 0.3400 |
| net_win_rate | 0.3949 |
| gross_profit_factor | 0.8725 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -11.5765 |
| sortino_ratio | -5.6427 |
| max_drawdown | 0.9993 |
| cagr | -0.9436 |
| net_avg_win | 11.0949 |
| net_avg_loss | -21.2953 |
| avg_hold_time_bars | 2.8026 |
| exposure | 0.1490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
