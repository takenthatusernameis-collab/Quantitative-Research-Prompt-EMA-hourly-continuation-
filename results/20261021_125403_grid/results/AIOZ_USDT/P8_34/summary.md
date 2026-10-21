# EMA Hourly Continuation — AIOZ/USDT P8_34

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.7433 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -2.8117 |
| sortino_ratio | -1.0668 |
| max_drawdown | 0.7454 |
| cagr | -0.3880 |
| net_avg_win | 61.0773 |
| net_avg_loss | -74.0153 |
| avg_hold_time_bars | 8.2426 |
| exposure | 0.2656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
