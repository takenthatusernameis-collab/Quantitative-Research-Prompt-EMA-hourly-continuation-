# EMA Hourly Continuation — STRAX/USDT P12_26

**Symbol:** STRAX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.4902 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.7398 |
| gross_win_rate | 0.4482 |
| sharpe_ratio | -5.1739 |
| sortino_ratio | -1.9274 |
| max_drawdown | 0.8907 |
| cagr | -0.5880 |
| net_avg_win | 28.2614 |
| net_avg_loss | -46.8378 |
| avg_hold_time_bars | 6.5488 |
| exposure | 0.2024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
