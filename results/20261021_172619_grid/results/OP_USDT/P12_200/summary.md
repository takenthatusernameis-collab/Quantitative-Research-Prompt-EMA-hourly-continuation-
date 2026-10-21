# EMA Hourly Continuation — OP/USDT P12_200

**Symbol:** OP/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 215 |
| net_profit_factor | 0.8892 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -0.5286 |
| sortino_ratio | -0.1109 |
| max_drawdown | 0.2144 |
| cagr | -0.0519 |
| net_avg_win | 92.2836 |
| net_avg_loss | -106.7231 |
| avg_hold_time_bars | 81.3535 |
| exposure | 0.7950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
