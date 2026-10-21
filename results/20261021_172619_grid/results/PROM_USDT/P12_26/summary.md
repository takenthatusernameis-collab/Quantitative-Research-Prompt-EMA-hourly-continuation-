# EMA Hourly Continuation — PROM/USDT P12_26

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.5887 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.9028 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -4.2903 |
| sortino_ratio | -1.4676 |
| max_drawdown | 0.8203 |
| cagr | -0.4936 |
| net_avg_win | 44.5734 |
| net_avg_loss | -63.8193 |
| avg_hold_time_bars | 6.8313 |
| exposure | 0.1785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
