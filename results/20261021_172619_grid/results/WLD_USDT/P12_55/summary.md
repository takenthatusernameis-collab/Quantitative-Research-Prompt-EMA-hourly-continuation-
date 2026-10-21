# EMA Hourly Continuation — WLD/USDT P12_55

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.8067 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -1.6926 |
| sortino_ratio | -0.5779 |
| max_drawdown | 0.5401 |
| cagr | -0.2349 |
| net_avg_win | 72.9698 |
| net_avg_loss | -87.0360 |
| avg_hold_time_bars | 13.8021 |
| exposure | 0.3582 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
