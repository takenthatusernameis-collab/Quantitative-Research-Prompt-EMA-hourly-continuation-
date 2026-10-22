# EMA Hourly Continuation — LINK/USDT P8_21

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1601 |
| net_profit_factor | 0.3629 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4722 |
| sharpe_ratio | -11.8635 |
| sortino_ratio | -6.6793 |
| max_drawdown | 0.9998 |
| cagr | -0.9684 |
| net_avg_win | 8.0210 |
| net_avg_loss | -17.6130 |
| avg_hold_time_bars | 2.9263 |
| exposure | 0.2130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
