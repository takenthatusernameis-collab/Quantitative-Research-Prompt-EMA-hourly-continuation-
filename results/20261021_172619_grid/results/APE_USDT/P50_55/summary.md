# EMA Hourly Continuation — APE/USDT P50_55

**Symbol:** APE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 105 |
| net_profit_factor | 0.7099 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4952 |
| sharpe_ratio | -1.0659 |
| sortino_ratio | -0.1568 |
| max_drawdown | 0.1716 |
| cagr | -0.0688 |
| net_avg_win | 77.1587 |
| net_avg_loss | -106.6378 |
| avg_hold_time_bars | 4.4190 |
| exposure | 0.0211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
