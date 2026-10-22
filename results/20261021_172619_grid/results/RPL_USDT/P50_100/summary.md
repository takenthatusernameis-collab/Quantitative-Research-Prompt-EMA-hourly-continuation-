# EMA Hourly Continuation — RPL/USDT P50_100

**Symbol:** RPL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6849 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9049 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -2.6690 |
| sortino_ratio | -0.7880 |
| max_drawdown | 0.6006 |
| cagr | -0.3022 |
| net_avg_win | 64.4892 |
| net_avg_loss | -82.2920 |
| avg_hold_time_bars | 10.3828 |
| exposure | 0.2025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
