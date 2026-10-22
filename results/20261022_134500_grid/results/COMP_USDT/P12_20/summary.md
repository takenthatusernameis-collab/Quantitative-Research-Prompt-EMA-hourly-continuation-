# EMA Hourly Continuation — COMP/USDT P12_20

**Symbol:** COMP/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1587 |
| net_profit_factor | 0.1634 |
| net_win_rate | 0.3743 |
| gross_profit_factor | 0.5390 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -15.8316 |
| sortino_ratio | -9.1021 |
| max_drawdown | 1.0000 |
| cagr | -0.9913 |
| net_avg_win | 3.2872 |
| net_avg_loss | -12.0368 |
| avg_hold_time_bars | 2.3819 |
| exposure | 0.1718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
