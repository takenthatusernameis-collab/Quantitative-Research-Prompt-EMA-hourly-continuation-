# EMA Hourly Continuation — DOGE/USDT P34_55

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.7028 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0185 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.6453 |
| sortino_ratio | -0.3824 |
| max_drawdown | 0.3741 |
| cagr | -0.1594 |
| net_avg_win | 62.8403 |
| net_avg_loss | -93.6403 |
| avg_hold_time_bars | 6.3000 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
