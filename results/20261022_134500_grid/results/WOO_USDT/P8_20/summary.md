# EMA Hourly Continuation — WOO/USDT P8_20

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1655 |
| net_profit_factor | 0.4173 |
| net_win_rate | 0.4193 |
| gross_profit_factor | 0.9010 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -11.7197 |
| sortino_ratio | -6.7193 |
| max_drawdown | 0.9998 |
| cagr | -0.9656 |
| net_avg_win | 10.3182 |
| net_avg_loss | -17.8550 |
| avg_hold_time_bars | 3.2320 |
| exposure | 0.2431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
