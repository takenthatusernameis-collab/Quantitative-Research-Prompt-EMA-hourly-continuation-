# EMA Hourly Continuation — ENA/USDT P144_200

**Symbol:** ENA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.7439 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9093 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.1569 |
| sortino_ratio | -0.2093 |
| max_drawdown | 0.2641 |
| cagr | -0.0920 |
| net_avg_win | 81.2343 |
| net_avg_loss | -100.0990 |
| avg_hold_time_bars | 6.5963 |
| exposure | 0.0483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
