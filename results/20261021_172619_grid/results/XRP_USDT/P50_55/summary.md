# EMA Hourly Continuation — XRP/USDT P50_55

**Symbol:** XRP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 82 |
| net_profit_factor | 0.5864 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 1.0344 |
| gross_win_rate | 0.5122 |
| sharpe_ratio | -1.3905 |
| sortino_ratio | -0.1822 |
| max_drawdown | 0.1836 |
| cagr | -0.0776 |
| net_avg_win | 65.0654 |
| net_avg_loss | -105.6775 |
| avg_hold_time_bars | 5.1098 |
| exposure | 0.0190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
