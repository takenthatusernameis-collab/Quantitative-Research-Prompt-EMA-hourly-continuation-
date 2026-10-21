# EMA Hourly Continuation — TRB/USDT P20_55

**Symbol:** TRB/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 520 |
| net_profit_factor | 0.5762 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4212 |
| sharpe_ratio | -4.2591 |
| sortino_ratio | -1.3734 |
| max_drawdown | 0.8009 |
| cagr | -0.4696 |
| net_avg_win | 49.5518 |
| net_avg_loss | -62.5662 |
| avg_hold_time_bars | 9.4846 |
| exposure | 0.2232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
