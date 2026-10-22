# EMA Hourly Continuation — DODO/USDT P12_34

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -3.6390 |
| sortino_ratio | -1.3463 |
| max_drawdown | 0.7893 |
| cagr | -0.4606 |
| net_avg_win | 47.4175 |
| net_avg_loss | -62.9334 |
| avg_hold_time_bars | 7.2692 |
| exposure | 0.2224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
