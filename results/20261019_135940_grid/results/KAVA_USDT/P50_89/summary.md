# EMA Hourly Continuation — KAVA/USDT P50_89

**Symbol:** KAVA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 742 |
| net_profit_factor | 0.4113 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.8089 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -8.6141 |
| sortino_ratio | -3.3398 |
| max_drawdown | 0.9858 |
| cagr | -0.8138 |
| net_avg_win | 22.9483 |
| net_avg_loss | -37.8683 |
| avg_hold_time_bars | 5.2871 |
| exposure | 0.1783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
