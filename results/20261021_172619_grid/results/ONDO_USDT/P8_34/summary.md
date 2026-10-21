# EMA Hourly Continuation — ONDO/USDT P8_34

**Symbol:** ONDO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.8827 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1166 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -0.9462 |
| sortino_ratio | -0.3545 |
| max_drawdown | 0.4049 |
| cagr | -0.1551 |
| net_avg_win | 72.7158 |
| net_avg_loss | -93.0685 |
| avg_hold_time_bars | 8.8633 |
| exposure | 0.2711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
