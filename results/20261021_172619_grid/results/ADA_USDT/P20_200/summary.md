# EMA Hourly Continuation — ADA/USDT P20_200

**Symbol:** ADA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.8692 |
| net_win_rate | 0.5161 |
| gross_profit_factor | 1.0489 |
| gross_win_rate | 0.5161 |
| sharpe_ratio | -0.6838 |
| sortino_ratio | -0.1638 |
| max_drawdown | 0.2615 |
| cagr | -0.0749 |
| net_avg_win | 81.8972 |
| net_avg_loss | -100.5070 |
| avg_hold_time_bars | 48.9211 |
| exposure | 0.6204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
