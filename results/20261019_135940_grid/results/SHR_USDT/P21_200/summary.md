# EMA Hourly Continuation — SHR/USDT P21_200

**Symbol:** SHR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.5467 |
| net_win_rate | 0.3859 |
| gross_profit_factor | 0.6928 |
| gross_win_rate | 0.3859 |
| sharpe_ratio | -5.5872 |
| sortino_ratio | -2.0226 |
| max_drawdown | 0.9170 |
| cagr | -0.6187 |
| net_avg_win | 41.9922 |
| net_avg_loss | -48.2578 |
| avg_hold_time_bars | 16.6053 |
| exposure | 0.5102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
