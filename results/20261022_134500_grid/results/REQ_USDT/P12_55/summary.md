# EMA Hourly Continuation — REQ/USDT P12_55

**Symbol:** REQ/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1126 |
| net_profit_factor | 0.4193 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.8106 |
| gross_win_rate | 0.4290 |
| sharpe_ratio | -10.6703 |
| sortino_ratio | -5.0739 |
| max_drawdown | 0.9984 |
| cagr | -0.9228 |
| net_avg_win | 16.2752 |
| net_avg_loss | -25.1739 |
| avg_hold_time_bars | 7.5710 |
| exposure | 0.3875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
