# EMA Hourly Continuation — ALGO/USDT P20_26

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 153 |
| net_profit_factor | 0.6991 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0126 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.3945 |
| sortino_ratio | -0.2483 |
| max_drawdown | 0.2788 |
| cagr | -0.1074 |
| net_avg_win | 74.9308 |
| net_avg_loss | -108.5886 |
| avg_hold_time_bars | 4.4902 |
| exposure | 0.0312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
