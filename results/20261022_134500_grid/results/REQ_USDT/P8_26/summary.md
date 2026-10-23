# EMA Hourly Continuation — REQ/USDT P8_26

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1593 |
| net_profit_factor | 0.3412 |
| net_win_rate | 0.3766 |
| gross_profit_factor | 0.7676 |
| gross_win_rate | 0.4181 |
| sharpe_ratio | -14.7526 |
| sortino_ratio | -8.4482 |
| max_drawdown | 1.0000 |
| cagr | -0.9866 |
| net_avg_win | 8.6322 |
| net_avg_loss | -15.2861 |
| avg_hold_time_bars | 4.3170 |
| exposure | 0.3126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
