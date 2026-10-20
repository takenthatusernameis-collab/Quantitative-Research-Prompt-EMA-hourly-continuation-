# EMA Hourly Continuation — OGN/USDT P26_55

**Symbol:** OGN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.4767 |
| net_win_rate | 0.4266 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -8.1330 |
| sortino_ratio | -3.4703 |
| max_drawdown | 0.9875 |
| cagr | -0.8209 |
| net_avg_win | 22.9375 |
| net_avg_loss | -35.7892 |
| avg_hold_time_bars | 4.8052 |
| exposure | 0.1998 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
