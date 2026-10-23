# EMA Hourly Continuation — SLP/USDT P55_89

**Symbol:** SLP/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5224 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.9851 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -6.4659 |
| sortino_ratio | -2.5198 |
| max_drawdown | 0.9557 |
| cagr | -0.7107 |
| net_avg_win | 30.3825 |
| net_avg_loss | -48.3274 |
| avg_hold_time_bars | 4.0923 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
