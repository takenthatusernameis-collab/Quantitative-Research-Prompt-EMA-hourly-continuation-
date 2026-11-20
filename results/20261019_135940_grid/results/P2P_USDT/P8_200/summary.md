# EMA Hourly Continuation — P2P/USDT P8_200

**Symbol:** P2P/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6282 |
| net_win_rate | 0.4320 |
| gross_profit_factor | 0.7799 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -2.7861 |
| sortino_ratio | -0.7584 |
| max_drawdown | 0.6055 |
| cagr | -0.3009 |
| net_avg_win | 61.8491 |
| net_avg_loss | -74.8785 |
| avg_hold_time_bars | 46.7653 |
| exposure | 0.7971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
