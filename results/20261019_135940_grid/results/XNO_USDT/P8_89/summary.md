# EMA Hourly Continuation — XNO/USDT P8_89

**Symbol:** XNO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.5112 |
| net_win_rate | 0.3942 |
| gross_profit_factor | 0.7577 |
| gross_win_rate | 0.4039 |
| sharpe_ratio | -7.7899 |
| sortino_ratio | -3.3326 |
| max_drawdown | 0.9833 |
| cagr | -0.8025 |
| net_avg_win | 28.0149 |
| net_avg_loss | -35.6582 |
| avg_hold_time_bars | 13.8539 |
| exposure | 0.5863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
