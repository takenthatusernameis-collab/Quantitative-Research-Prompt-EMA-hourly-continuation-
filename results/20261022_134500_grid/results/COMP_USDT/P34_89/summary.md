# EMA Hourly Continuation — COMP/USDT P34_89

**Symbol:** COMP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4783 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.8634 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -5.2534 |
| sortino_ratio | -1.9816 |
| max_drawdown | 0.9150 |
| cagr | -0.6209 |
| net_avg_win | 24.4599 |
| net_avg_loss | -45.6662 |
| avg_hold_time_bars | 8.1779 |
| exposure | 0.2695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
