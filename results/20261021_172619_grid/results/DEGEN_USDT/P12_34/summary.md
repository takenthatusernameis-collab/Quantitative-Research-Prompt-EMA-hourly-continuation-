# EMA Hourly Continuation — DEGEN/USDT P12_34

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.8201 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.4975 |
| sharpe_ratio | -1.7433 |
| sortino_ratio | -0.6069 |
| max_drawdown | 0.5859 |
| cagr | -0.2452 |
| net_avg_win | 78.4573 |
| net_avg_loss | -94.7020 |
| avg_hold_time_bars | 7.8680 |
| exposure | 0.2117 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
