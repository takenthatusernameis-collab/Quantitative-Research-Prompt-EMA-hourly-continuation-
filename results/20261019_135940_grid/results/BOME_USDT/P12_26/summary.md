# EMA Hourly Continuation — BOME/USDT P12_26

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1426 |
| net_profit_factor | 0.4499 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.8583 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -9.3911 |
| sortino_ratio | -4.9825 |
| max_drawdown | 0.9981 |
| cagr | -0.9156 |
| net_avg_win | 13.0152 |
| net_avg_loss | -22.7039 |
| avg_hold_time_bars | 2.5589 |
| exposure | 0.1659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
