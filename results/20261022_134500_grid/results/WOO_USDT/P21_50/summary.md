# EMA Hourly Continuation — WOO/USDT P21_50

**Symbol:** WOO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 928 |
| net_profit_factor | 0.5976 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.9940 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -6.0814 |
| sortino_ratio | -2.6128 |
| max_drawdown | 0.9606 |
| cagr | -0.7156 |
| net_avg_win | 33.2259 |
| net_avg_loss | -47.5912 |
| avg_hold_time_bars | 5.1821 |
| exposure | 0.2186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
