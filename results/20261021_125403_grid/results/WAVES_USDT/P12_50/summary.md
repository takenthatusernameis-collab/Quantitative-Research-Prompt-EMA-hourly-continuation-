# EMA Hourly Continuation — WAVES/USDT P12_50

**Symbol:** WAVES/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.6494 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8885 |
| gross_win_rate | 0.4659 |
| sharpe_ratio | -3.8200 |
| sortino_ratio | -1.4131 |
| max_drawdown | 0.8099 |
| cagr | -0.4805 |
| net_avg_win | 47.5892 |
| net_avg_loss | -63.9215 |
| avg_hold_time_bars | 9.7196 |
| exposure | 0.2978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
