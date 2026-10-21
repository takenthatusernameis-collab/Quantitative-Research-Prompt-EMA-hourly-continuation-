# EMA Hourly Continuation — ELON/USDT P34_50

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.6751 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9638 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.6744 |
| sortino_ratio | -0.3307 |
| max_drawdown | 0.3159 |
| cagr | -0.1403 |
| net_avg_win | 70.6005 |
| net_avg_loss | -101.3050 |
| avg_hold_time_bars | 5.7778 |
| exposure | 0.0496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
