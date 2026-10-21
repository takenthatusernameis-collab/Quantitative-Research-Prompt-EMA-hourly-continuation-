# EMA Hourly Continuation — SLP/USDT P20_55

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.7129 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -3.3767 |
| sortino_ratio | -1.1769 |
| max_drawdown | 0.7759 |
| cagr | -0.4174 |
| net_avg_win | 66.3130 |
| net_avg_loss | -81.0654 |
| avg_hold_time_bars | 8.0871 |
| exposure | 0.2195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
