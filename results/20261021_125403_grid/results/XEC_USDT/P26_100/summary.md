# EMA Hourly Continuation — XEC/USDT P26_100

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 545 |
| net_profit_factor | 0.7786 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0553 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.8530 |
| sortino_ratio | -0.6204 |
| max_drawdown | 0.5725 |
| cagr | -0.2479 |
| net_avg_win | 64.3788 |
| net_avg_loss | -87.3657 |
| avg_hold_time_bars | 14.3835 |
| exposure | 0.3547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
