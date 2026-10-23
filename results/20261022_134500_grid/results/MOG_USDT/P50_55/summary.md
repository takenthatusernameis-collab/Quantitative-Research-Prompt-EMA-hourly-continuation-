# EMA Hourly Continuation — MOG/USDT P50_55

**Symbol:** MOG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.2834 |
| net_win_rate | 0.3736 |
| gross_profit_factor | 0.5490 |
| gross_win_rate | 0.3991 |
| sharpe_ratio | -10.3092 |
| sortino_ratio | -4.0963 |
| max_drawdown | 0.9927 |
| cagr | -0.8826 |
| net_avg_win | 14.9300 |
| net_avg_loss | -31.4139 |
| avg_hold_time_bars | 1.9190 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
