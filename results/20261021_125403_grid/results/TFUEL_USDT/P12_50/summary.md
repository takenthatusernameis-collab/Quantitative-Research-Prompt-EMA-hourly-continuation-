# EMA Hourly Continuation — TFUEL/USDT P12_50

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.5927 |
| net_win_rate | 0.4226 |
| gross_profit_factor | 0.7969 |
| gross_win_rate | 0.4226 |
| sharpe_ratio | -5.3798 |
| sortino_ratio | -2.0763 |
| max_drawdown | 0.9105 |
| cagr | -0.6159 |
| net_avg_win | 42.1959 |
| net_avg_loss | -52.1083 |
| avg_hold_time_bars | 8.6676 |
| exposure | 0.2914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
