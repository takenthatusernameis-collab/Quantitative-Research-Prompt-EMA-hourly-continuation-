# EMA Hourly Continuation — BLUR/USDT P12_34

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.4887 |
| sortino_ratio | -1.2724 |
| max_drawdown | 0.7800 |
| cagr | -0.4416 |
| net_avg_win | 46.5734 |
| net_avg_loss | -62.5412 |
| avg_hold_time_bars | 6.4384 |
| exposure | 0.1914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
