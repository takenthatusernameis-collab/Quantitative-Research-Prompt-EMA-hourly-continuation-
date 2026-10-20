# EMA Hourly Continuation — AVA/USDT P12_55

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 990 |
| net_profit_factor | 0.5220 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8531 |
| gross_win_rate | 0.4707 |
| sharpe_ratio | -6.3110 |
| sortino_ratio | -2.7965 |
| max_drawdown | 0.9716 |
| cagr | -0.7420 |
| net_avg_win | 23.1503 |
| net_avg_loss | -37.8718 |
| avg_hold_time_bars | 7.7404 |
| exposure | 0.3483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
