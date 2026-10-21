# EMA Hourly Continuation — CETUS/USDT P34_100

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7682 |
| net_win_rate | 0.4876 |
| gross_profit_factor | 0.9494 |
| gross_win_rate | 0.4876 |
| sharpe_ratio | -1.7568 |
| sortino_ratio | -0.5278 |
| max_drawdown | 0.4742 |
| cagr | -0.2169 |
| net_avg_win | 70.3118 |
| net_avg_loss | -87.1092 |
| avg_hold_time_bars | 13.8427 |
| exposure | 0.2788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
