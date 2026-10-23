# EMA Hourly Continuation — KAVA/USDT P50_55

**Symbol:** KAVA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.1927 |
| net_win_rate | 0.3009 |
| gross_profit_factor | 0.7319 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -14.9625 |
| sortino_ratio | -6.8924 |
| max_drawdown | 0.9999 |
| cagr | -0.9761 |
| net_avg_win | 8.5863 |
| net_avg_loss | -19.1736 |
| avg_hold_time_bars | 2.3907 |
| exposure | 0.1004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
