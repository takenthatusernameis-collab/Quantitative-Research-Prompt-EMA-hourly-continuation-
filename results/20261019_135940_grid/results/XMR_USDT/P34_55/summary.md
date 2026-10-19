# EMA Hourly Continuation — XMR/USDT P34_55

**Symbol:** XMR/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1264 |
| net_profit_factor | 0.2060 |
| net_win_rate | 0.3528 |
| gross_profit_factor | 0.6374 |
| gross_win_rate | 0.3805 |
| sharpe_ratio | -14.7927 |
| sortino_ratio | -7.6194 |
| max_drawdown | 1.0000 |
| cagr | -0.9824 |
| net_avg_win | 5.8163 |
| net_avg_loss | -15.3957 |
| avg_hold_time_bars | 2.1400 |
| exposure | 0.1230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
