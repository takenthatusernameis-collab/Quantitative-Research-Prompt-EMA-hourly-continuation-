# EMA Hourly Continuation — SUN/USDT P20_34

**Symbol:** SUN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1004 |
| net_profit_factor | 0.1334 |
| net_win_rate | 0.3147 |
| gross_profit_factor | 0.6355 |
| gross_win_rate | 0.4044 |
| sharpe_ratio | -15.0928 |
| sortino_ratio | -7.1646 |
| max_drawdown | 0.9999 |
| cagr | -0.9787 |
| net_avg_win | 4.8692 |
| net_avg_loss | -16.7704 |
| avg_hold_time_bars | 4.1673 |
| exposure | 0.1893 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
