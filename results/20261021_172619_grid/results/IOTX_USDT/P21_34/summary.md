# EMA Hourly Continuation — IOTX/USDT P21_34

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.7416 |
| net_win_rate | 0.5270 |
| gross_profit_factor | 1.0935 |
| gross_win_rate | 0.5270 |
| sharpe_ratio | -1.5792 |
| sortino_ratio | -0.4050 |
| max_drawdown | 0.4294 |
| cagr | -0.1684 |
| net_avg_win | 64.0793 |
| net_avg_loss | -96.2693 |
| avg_hold_time_bars | 5.2222 |
| exposure | 0.0748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
