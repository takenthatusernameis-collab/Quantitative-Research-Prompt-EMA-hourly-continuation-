# EMA Hourly Continuation — WOO/USDT P8_26

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1535 |
| net_profit_factor | 0.5259 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.9988 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -9.1026 |
| sortino_ratio | -5.0173 |
| max_drawdown | 0.9979 |
| cagr | -0.9139 |
| net_avg_win | 16.1131 |
| net_avg_loss | -24.8213 |
| avg_hold_time_bars | 4.1492 |
| exposure | 0.2895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
