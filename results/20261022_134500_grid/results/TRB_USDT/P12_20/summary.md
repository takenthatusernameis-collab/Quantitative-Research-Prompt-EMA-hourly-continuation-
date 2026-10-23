# EMA Hourly Continuation — TRB/USDT P12_20

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1618 |
| net_profit_factor | 0.2680 |
| net_win_rate | 0.3616 |
| gross_profit_factor | 0.6950 |
| gross_win_rate | 0.4030 |
| sharpe_ratio | -16.0155 |
| sortino_ratio | -9.2316 |
| max_drawdown | 1.0000 |
| cagr | -0.9920 |
| net_avg_win | 6.2581 |
| net_avg_loss | -13.2245 |
| avg_hold_time_bars | 2.1477 |
| exposure | 0.1572 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
