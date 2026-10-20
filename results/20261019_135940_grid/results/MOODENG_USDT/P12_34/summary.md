# EMA Hourly Continuation — MOODENG/USDT P12_34

**Symbol:** MOODENG/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.5615 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.8581 |
| gross_win_rate | 0.4540 |
| sharpe_ratio | -8.1775 |
| sortino_ratio | -4.1238 |
| max_drawdown | 0.9872 |
| cagr | -0.8718 |
| net_avg_win | 26.6196 |
| net_avg_loss | -37.3931 |
| avg_hold_time_bars | 4.1330 |
| exposure | 0.2458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
